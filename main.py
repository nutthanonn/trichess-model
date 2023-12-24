import asyncio
import random
import time
import MESSAGE
import Trichess
import algorithm
import threading

async def wait_connection(trichess):
    while True:
        try:
            game_start = await trichess.receive_response()
            if game_start['Status'] != "Success":
                return
        except:
            pass

        time.sleep(0.25)

async def wait_my_turn(trichess):
    while True:
        try:
            await trichess.check_turn()
            turn_response = await trichess.receive_response()

            if turn_response['Status'] == "Success":
                if turn_response['YourTurn']:

                    board = turn_response['Board']
                    enemy_piece = []

                    for piece in board:
                        if piece['Owner'] != trichess.Player:
                            enemy_piece.append(piece)
                    
                    print(MESSAGE.ENEMY_PIECE)

                    return turn_response, enemy_piece
        except:
            pass

        time.sleep(0.25)

async def get_my_piece(trichess):
    while True:
        await trichess.myPiece()
        my_piece_response = await trichess.receive_response()

        if my_piece_response['Status'] == 'Success':
            if 'Check board for piece' in my_piece_response['Message']:
                trichess.Piece = my_piece_response['Board']
                break
            
        time.sleep(0.25)

    return None

async def check_my_king(trichess):
    while True:
        try:
            print(f"Wait to checking my king")

            await trichess.check_king()
            response = await trichess.receive_response()

            # print(response)
            move_able = []

            if response['Status'] == 'Success':
                if 'not in checked' in response['Message']:
                    break

                if response['KingInCheck'] and 'in checked' in response['Message']:
                    for move in response['KingMovableField']:
                        move_able.append(move['Field'])
                    break
                
            time.sleep(0.25)
        except:
            pass

    return move_able

async def get_all_possible_move(trichess):
    field = {}
    for current_place in trichess.Piece:
        current_place = current_place['Field']
        
        await trichess.move_able(current_place)
        piece_movable = await trichess.receive_response()

        # handle no movable
        if piece_movable['Status'] == 'Fail' and 'no movable' in piece_movable['Message']:
            print("No movable")
            continue

        if piece_movable['Status'] == 'Success':
            # print(f'Test on {current_place} success')
            if 'MovableFields' in piece_movable['Message']:
                for val in piece_movable['MovableFields']:
                    if current_place not in field:
                        field[current_place] = []

                    field[current_place].append(val['Field'])
                    
    return field

async def get_all_enemy_possible_move(trichess):
    print("Try to get all enemy possible move")
    field = {}
    for current_place in trichess.enemyPiece:
        current_place = current_place['Field']
        
        await trichess.move_able(current_place)
        piece_movable = await trichess.receive_response()

        # handle no movable
        if piece_movable['Status'] == 'Fail' and 'no movable' in piece_movable['Message']:
            print("No movable")
            continue

        if piece_movable['Status'] == 'Success':
            # print(f'Test on {current_place} success')
            if 'MovableFields' in piece_movable['Message']:
                for val in piece_movable['MovableFields']:
                    if current_place not in field:
                        field[current_place] = []

                    field[current_place].append(val['Field'])
                    
    return field

def check_pass(possible_move):
    return all(len(value) == 0 for value in possible_move.values())


async def main(url, type_algorithm, reconnect=False):
    count_turn = 0
    trichess = Trichess.Trichess(url)
    await trichess.connect()

    # loop wait to connect to game
    await wait_connection(trichess)
    
    # loop playgame
    while True:
        # loop wait my turn
        try:
            turn_res = await wait_my_turn(trichess)
            if turn_res:
                print(MESSAGE.MY_TURN)
                print(count_turn)
                trichess.Board, trichess.enemyPiece = turn_res

                # await get_my_piece(trichess)
                # possible_move = await get_all_possible_move(trichess)
                # print("Success get all possible move")

                check_king = await check_my_king(trichess)

                if check_king:
                    print(f"My king is in check king have moveable {check_king}")
                    for board in trichess.Board['Board']:
                        if board['Piece'] == 'King' and board['Owner'] == trichess.Player:
                            curr_position = board['Field']
                            break
                    
                    # ถ้า checking แล้ว king กินได้ให้กินเลย
                    check_eat = False
                    for king_move in check_king:
                        for enemy_piece in trichess.enemyPiece:
                            if enemy_piece['Field'] == king_move:
                                move_to = king_move
                                check_eat = True
                                break

                    if not check_eat:
                        print("Random move king")
                        move_to = random.choice(check_king)

                    print(f'My king is in check so I move {curr_position} to {move_to}')
                else:
                    await get_my_piece(trichess)
                    possible_move = await get_all_possible_move(trichess)
                    print("Success get all possible move")

                    enemy_possible_move = await get_all_enemy_possible_move(trichess)
                    print("Success get all enemy move")

                    # TODO: check if all possible move is None
                    if check_pass(possible_move):
                        await trichess.pass_turn()
                        pass_response = await trichess.receive_response()
                        if pass_response['Status'] == 'Success':
                            print(MESSAGE.PASS)
                        continue

                    curr_position, move_to = algorithm.algorithm_provider(
                        enemy_possible_move,
                        possible_move,
                        trichess.Board,
                        type_algorithm,
                        trichess.Player,
                        count_turn
                    )
                
                await trichess.send_move(curr_position, move_to)
                move_response = await trichess.receive_response()

                if move_response['Status'] == 'Success':
                    print(MESSAGE.MOVE_SUCCESS)
                    
                    await trichess.promote()
                    promote_response = await trichess.receive_response()
                    print(f"This is promote response: {promote_response}")
                    if promote_response['Status'] == 'Success':
                        print("PROMOTE SUCCESS")

                count_turn += 1
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break
            
        time.sleep(1)

if __name__ == '__main__':
    URL = 'ws://192.168.1.100:8181/game'
    asyncio.run(main(URL, 2),)
    # n_player = int(input("Enter number of player [int]: "))
    # URL = input("Enter URL: ")
    
    # for i in range(n_player):
    #     print(f"Select algorithm for player {i+1}")
    #     print(MESSAGE.ALGORITHM)
    #     algo = 2
        
    #     threading.Thread(target=asyncio.run, args=(main(URL, algo),)).start()
    #     print("Thread: ", i, " started")

    #     time.sleep(0.25)