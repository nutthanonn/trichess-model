import asyncio
import time
import MESSAGE
import Trichess
import random


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
    await trichess.myPiece()
    my_piece_response = await trichess.receive_response()

    if my_piece_response['Status'] == 'Success':
        trichess.Piece = my_piece_response['Board']

    # handle status not success
    else:
        while True:
            await trichess.myPiece()
            my_piece_response = await trichess.receive_response()
            if my_piece_response['Status'] == 'Success':
                trichess.Piece = my_piece_response['Board']
                break

            time.sleep(1)

    print(f"This is samle of piece {trichess.Piece[5:]}")

    return None

async def get_all_possible_move(trichess):
    # fix because this will recv my piece response

    field = {}
    for current_place in trichess.Piece:
        await trichess.move_able(current_place)
        piece_movable = await trichess.receive_response()
        print(f'Test on {current_place}')

        if piece_movable['Status'] == 'Success' and piece_movable['MovableFields']:
            for val in piece_movable['MovableFields']:
                field[current_place].append(val['Field'])

        # handle status not success
        else:
            while True:
                await trichess.move_able(current_place)
                piece_movable = await trichess.receive_response()
                print(f'Test on {current_place} again because status not success')
                if piece_movable['Status'] == 'Success' and piece_movable['MovableFields']:
                    for val in piece_movable['MovableFields']:
                        field[current_place].append(val['Field'])
                    break

                time.sleep(1)
                    
    return field

def play_random(possible_move):
    random_piece = random.choice(list(possible_move.keys()))
    random_move = random.choice(possible_move[random_piece])

    print(f"This is random piece: {random_piece} and random move: {random_move}")

    return random_piece, random_move


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

            random_piece, random_move = play_random(possible_move)
            
            await trichess.send_move(random_piece, random_move)
            move_response = await trichess.receive_response()

            if move_response['Status'] == 'Success':
                print(MESSAGE.MOVE_SUCCESS)

if __name__ == '__main__':
    URL = 'ws://192.168.1.100:8181/game'
    # URL = input("Enter URL: ")
    asyncio.run(main(URL))