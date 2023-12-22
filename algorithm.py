'''

This is enemy possible move:  {'GA2': ['GA4'], 'GB1': ['GC3', 'GA3', 'GC3'], 'GB2': ['GB4'], 'GC2': ['GC4'], 'GD2': ['GD4'], 'GE2': ['GE4'], 'GF2': ['GF4'], 'GG1': ['GH3', 'GF3', 'GH3'], 'GG2': ['GG4'], 'GH2': ['GH4'], 'RA2': ['RA4'], 'RB1': ['RC3', 'RA3', 'RC3'], 'RB2': ['RB4'], 'RC2': ['RC4'], 'RD2': ['RD4'], 'RE2': ['RE4'], 'RF2': ['RF4'], 'RG1': ['RH3', 'RF3', 'RH3'], 'RG2': ['RG4'], 'RH2': ['RH4']}
This is possible move:  {'BB1': ['BC3', 'BA3', 'BC3'], 'BB2': ['BB4'], 'BC2': ['BC4'], 'BD2': ['BD4'], 'BE2': ['BE4'], 'BF2': ['BF4'], 'BG1': ['BH3', 'BF3', 'BH3'], 'BG2': ['BG4'], 'BH2': ['BH4']}
This is current board:  [{'Field': 'BA1', 'Piece': 'Rook', 'Owner': 'Player1'}, {'Field': 'BA2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BB1', 'Piece': 'Knight', 'Owner': 'Player1'}, {'Field': 'BB2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BC1', 'Piece': 'Bishop', 'Owner': 'Player1'}, {'Field': 'BC2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BD1', 'Piece': 'Queen', 'Owner': 'Player1'}, {'Field': 'BD2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BE1', 'Piece': 'King', 'Owner': 'Player1'}, {'Field': 'BE2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BF1', 'Piece': 'Bishop', 'Owner': 'Player1'}, {'Field': 'BF2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BG1', 'Piece': 'Knight', 'Owner': 'Player1'}, {'Field': 'BG2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BH1', 'Piece': 'Rook', 'Owner': 'Player1'}, {'Field': 'BH2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'GA1', 'Piece': 'Rook', 'Owner': 'Player2'}, {'Field': 'GA2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GB1', 'Piece': 'Knight', 'Owner': 'Player2'}, {'Field': 'GB2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GC1', 'Piece': 'Bishop', 'Owner': 'Player2'}, {'Field': 'GC2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GD1', 'Piece': 'Queen', 'Owner': 'Player2'}, {'Field': 'GD2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GE1', 'Piece': 'King', 'Owner': 'Player2'}, {'Field': 'GE2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GF1', 'Piece': 'Bishop', 'Owner': 'Player2'}, {'Field': 'GF2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GG1', 'Piece': 'Knight', 'Owner': 'Player2'}, {'Field': 'GG2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GH1', 'Piece': 'Rook', 'Owner': 'Player2'}, {'Field': 'GH2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'RA1', 'Piece': 'Rook', 'Owner': 'Player3'}, {'Field': 'RA2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RB1', 'Piece': 'Knight', 'Owner': 'Player3'}, {'Field': 'RB2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RC1', 'Piece': 'Bishop', 'Owner': 'Player3'}, {'Field': 'RC2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RD1', 'Piece': 'Queen', 'Owner': 'Player3'}, {'Field': 'RD2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RE1', 'Piece': 'King', 'Owner': 'Player3'}, {'Field': 'RE2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RF1', 'Piece': 'Bishop', 'Owner': 'Player3'}, {'Field': 'RF2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RG1', 'Piece': 'Knight', 'Owner': 'Player3'}, {'Field': 'RG2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RH1', 'Piece': 'Rook', 'Owner': 'Player3'}, {'Field': 'RH2', 'Piece': 'Pawn', 'Owner': 'Player3'}]

'''

import random
import MESSAGE
import time

VALUE_PIECE = {
    "King": 1000,
    "Queen": 9,
    "Rook": 5,
    "Knight": 3,
    "Bishop": 3,
    "Pawn": 1
}

def algorithm_provider(enemy_possible_move, possible_move, current_board, type_algorithm, current_player):
    if type_algorithm == 1:
        return play_random(possible_move)
    elif type_algorithm == 2:
        return eat_priority_first(enemy_possible_move, possible_move, current_board, current_player)
    else:
        return play_random(possible_move)
    


def play_random(possible_move):
    while True:
        try:
            print("This is possible move: ", possible_move)

            random_piece = random.choice(list(possible_move.keys()))
            random_move = random.choice(possible_move[random_piece])

            print(f"This is random piece: {random_piece} and random move: {random_move}")

            return random_piece, random_move
        except:
            pass

        time.sleep(1)

def walk_dodge(enemy_possible_move, possible_move, current_board, current_player):
    dodge_moves = set()

    for piece, enemy_moves in enemy_possible_move.items():
        for enemy_move_field in enemy_moves:
            for board in current_board:
                if enemy_move_field == board['Field'] and board['Owner'] == current_player:
                    # The current player's piece is under threat, find possible dodge moves
                    for move_field in possible_move.get(piece, []):
                        dodge_moves.add(move_field)

    # Filter out duplicate dodge moves
    dodge_moves = list(set(dodge_moves))
    
    print("Dodge moves: ", dodge_moves)
    
    if not dodge_moves:
        return None
    
    # Select a random dodge move
    random_dodge_move = random.choice(dodge_moves)
    
    print(f"Selected dodge move: {random_dodge_move}")

    return piece, random_dodge_move

def walk_but_dont_eat(enemy_possible_move, possible_move, current_board, current_player):
    block_move = set(move_field for moves in enemy_possible_move.values() for move_field in moves)
    print("This is block move: ", block_move)

    piece, random_dodge = walk_dodge(enemy_possible_move, possible_move, current_board, current_player)
    
    if random_dodge is not None:
        return piece, random_dodge

    
    min_value = float('inf')
    min_piece = None
    min_move = None

    for piece, moves in possible_move.items():
        for move_field in moves:
            for board in current_board:
                if board['Owner'] == current_player and move_field not in block_move:
                    piece_value = VALUE_PIECE[board['Piece']]
                    if piece_value < min_value or (piece_value == min_value and piece < min_piece):
                        min_value = piece_value
                        min_piece = piece
                        min_move = move_field
    
    print(f"This is min piece: {min_piece} and min move: {min_move}")

    return min_piece, min_move
                

def eat_priority_first(enemy_possible_move, possible_move, current_board, current_player):
    current_board = current_board['Board']
    print("Calculate eat priority first")

    print(MESSAGE.ENEMY)

    print("This is enemy possible move: ", enemy_possible_move)
    print("This is possible move: ", possible_move)
    print("This is current board: ", current_board)

    max_value = 0
    max_piece = None
    max_move = None

    for piece, move in possible_move.items():
        for move_field in move:
            for board in current_board:
                if move_field == board['Field']:
                    if VALUE_PIECE[board['Piece']] > max_value and board['Owner'] != current_player:
                        max_value = VALUE_PIECE[board['Piece']]
                        max_piece = piece
                        max_move = move_field

                    if VALUE_PIECE[board['Piece']] == max_value and board['Owner'] != current_player:
                        if max_piece < piece:
                            max_piece = piece
                            max_move = move_field

    print(f"This is max piece: {max_piece} and max move: {max_move}")

    if max_piece is None or max_move is None:
        return walk_but_dont_eat(enemy_possible_move, possible_move, current_board, current_player)
    
    # if max_move in enemy_possible_move.get(max_piece, []):
    #     print("Selected move is not safe, finding alternative.")

    return max_piece, max_move

def check_8(target):
    swap_color = {"GA":"RH", "GB":"RG", "GC":"RF", "GD":"RE", "GE":"BD", "GF":"BC", "GG":"BB", "GH":"BA",
                  "BA":"GH", "BB":"GG", "BC":"GF", "BD":"GE", "BE":"RD", "BF":"RC", "BG":"RB", "BH":"RA",
                  "RA":"BH", "RB":"BG", "RC":"BF", "RD":"BE", "RE":"GD", "RF":"GC", "RG":"GB", "RH":"GA",}
    board_dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
    board_list = ["A","B","C","D","E","F","G","H"]
    number_list = ["1","2","3","4","4","3","2","1"]
    straight = ["Queen", "Rook"]
    oblique = ["Queen", "Bishop"]

    # ไม่เล่นตรงกลาง
    if((target[2] == "E" or target[2] == "D") and target[3] == "4"):
        return
    
    # for i in range(9):
    #     check = False
        # target[0] + target[1] + target[2]
        

        """ concept for loop check if found enemy break small loop if its cant eat that continue but if can eat break   """

        #straight

        # check A B C D E F G H
        for ii in range(board_dict[target[1]], 9):
            #check
            target[0] + board_list[ii] + target[2]
            break

        for ii in range(board_dict[target[1]], -1, -1):
            #check
            target[0] + board_list[ii] + target[2]
            break
        
        #check 1 2 3 4 4 3 2 1
        for ii in range(int(target[2]), 5):
            break
        for iii in range(4, 0, -1):
                #switch color
                check
                break
        
        for ii in range(int(target[2]), 0, -1):
            break


        #oblique

        # No switch color
        count = 0
        for ii in range(int(target[2]), 0, -1):
            count += 1
            board_list[board_dict[target[1]] - count]
            break

        count = 0
        for ii in range(int(target[2]), 0, -1):
            count += 1
            board_list[board_dict[target[1]] + count]
            break
        
        #switch color
        count = 0
        for ii in range(int(target[2]), 5):
            count += 1
            board_list[board_dict[target[1]] + count]
            break
        for iii in range(4, 0, -1):
            #switch color
            count += 1
            board_list[board_dict[target[1]] + count]
            break

        count = 0
        for ii in range(int(target[2]), 5):
            count += 1
            board_list[board_dict[target[1]] - count]
            break
        for iii in range(4, 0, -1):
            #switch color
            count += 1
            board_list[board_dict[target[1]] - count]
            # if board_list[board_dict[target[1]] - count] == "H" or board_list[board_dict[target[1]] - count] == "A":
                # break


    current_board = current_board['Board']
