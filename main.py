import asyncio
import time
import MESSAGE
import Trichess
import algorithm



async def wait_connection(trichess):
    while True:
        try:
            game_start = await trichess.receive_response()
            print("Fuck you game: ", game_start)
            if game_start['Status'] != "Success":
                return
        except:
            pass

        time.sleep(1)

async def wait_my_turn(trichess):
    while True:
        try:
            await trichess.check_turn()
            turn_response = await trichess.receive_response()

            if turn_response['Status'] == "Success":
                if turn_response['YourTurn']:
                    return turn_response
        except:
            pass

        time.sleep(1)

async def get_my_piece(trichess):
    while True:
        await trichess.myPiece()
        my_piece_response = await trichess.receive_response()

        if my_piece_response['Status'] == 'Success':
            if 'Check board for piece' in my_piece_response['Message']:
                trichess.Piece = my_piece_response['Board']
                break
            
        time.sleep(1)

    print(f"This is samle of piece {trichess.Piece[:5]}")
    return None


async def get_all_possible_move(trichess):
    field = {}
    for current_place in trichess.Piece:
        current_place = current_place['Field']
        
        await trichess.move_able(current_place)
        piece_movable = await trichess.receive_response()

        # handle no movable
        if piece_movable['Status'] == 'Fail' and 'no movable' in piece_movable['Message']:
            continue

        if piece_movable['Status'] == 'Success':
            print(f'Test on {current_place} success')
            if 'MovableFields' in piece_movable['Message']:
                for val in piece_movable['MovableFields']:
                    if current_place not in field:
                        field[current_place] = []
                    else:
                        field[current_place].append(val['Field'])
                    
    return field

async def main(url):
    trichess = Trichess.Trichess(url)
    await trichess.connect()

    # loop wait to connect to game
    await wait_connection(trichess)
    
    # loop playgame
    while True:
        # loop wait my turn
        turn_response = await wait_my_turn(trichess)
        if turn_response:
            print(MESSAGE.MY_TURN)
            trichess.Board = turn_response['Board']

            await get_my_piece(trichess)
            
            possible_move = await get_all_possible_move(trichess)

            print("This is possible move: ", possible_move)

            random_piece, random_move = algorithm.play_random(possible_move)
            
            await trichess.send_move(random_piece, random_move)
            move_response = await trichess.receive_response()

            if move_response['Status'] == 'Success':
                print(MESSAGE.MOVE_SUCCESS)
        
        time.sleep(1)

if __name__ == '__main__':
    URL = 'ws://192.168.1.100:8181/game'
    # URL = input("Enter URL: ")
    asyncio.run(main(URL))