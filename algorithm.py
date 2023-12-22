'''

This is enemy possible move:  {'GA2': ['GA4'], 'GB1': ['GC3', 'GA3', 'GC3'], 'GB2': ['GB4'], 'GC2': ['GC4'], 'GD2': ['GD4'], 'GE2': ['GE4'], 'GF2': ['GF4'], 'GG1': ['GH3', 'GF3', 'GH3'], 'GG2': ['GG4'], 'GH2': ['GH4'], 'RA2': ['RA4'], 'RB1': ['RC3', 'RA3', 'RC3'], 'RB2': ['RB4'], 'RC2': ['RC4'], 'RD2': ['RD4'], 'RE2': ['RE4'], 'RF2': ['RF4'], 'RG1': ['RH3', 'RF3', 'RH3'], 'RG2': ['RG4'], 'RH2': ['RH4']}
This is possible move:  {'BB1': ['BC3', 'BA3', 'BC3'], 'BB2': ['BB4'], 'BC2': ['BC4'], 'BD2': ['BD4'], 'BE2': ['BE4'], 'BF2': ['BF4'], 'BG1': ['BH3', 'BF3', 'BH3'], 'BG2': ['BG4'], 'BH2': ['BH4']}
This is current board:  [{'Field': 'BA1', 'Piece': 'Rook', 'Owner': 'Player1'}, {'Field': 'BA2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BB1', 'Piece': 'Knight', 'Owner': 'Player1'}, {'Field': 'BB2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BC1', 'Piece': 'Bishop', 'Owner': 'Player1'}, {'Field': 'BC2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BD1', 'Piece': 'Queen', 'Owner': 'Player1'}, {'Field': 'BD2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BE1', 'Piece': 'King', 'Owner': 'Player1'}, {'Field': 'BE2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BF1', 'Piece': 'Bishop', 'Owner': 'Player1'}, {'Field': 'BF2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BG1', 'Piece': 'Knight', 'Owner': 'Player1'}, {'Field': 'BG2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'BH1', 'Piece': 'Rook', 'Owner': 'Player1'}, {'Field': 'BH2', 'Piece': 'Pawn', 'Owner': 'Player1'}, {'Field': 'GA1', 'Piece': 'Rook', 'Owner': 'Player2'}, {'Field': 'GA2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GB1', 'Piece': 'Knight', 'Owner': 'Player2'}, {'Field': 'GB2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GC1', 'Piece': 'Bishop', 'Owner': 'Player2'}, {'Field': 'GC2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GD1', 'Piece': 'Queen', 'Owner': 'Player2'}, {'Field': 'GD2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GE1', 'Piece': 'King', 'Owner': 'Player2'}, {'Field': 'GE2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GF1', 'Piece': 'Bishop', 'Owner': 'Player2'}, {'Field': 'GF2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GG1', 'Piece': 'Knight', 'Owner': 'Player2'}, {'Field': 'GG2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'GH1', 'Piece': 'Rook', 'Owner': 'Player2'}, {'Field': 'GH2', 'Piece': 'Pawn', 'Owner': 'Player2'}, {'Field': 'RA1', 'Piece': 'Rook', 'Owner': 'Player3'}, {'Field': 'RA2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RB1', 'Piece': 'Knight', 'Owner': 'Player3'}, {'Field': 'RB2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RC1', 'Piece': 'Bishop', 'Owner': 'Player3'}, {'Field': 'RC2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RD1', 'Piece': 'Queen', 'Owner': 'Player3'}, {'Field': 'RD2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RE1', 'Piece': 'King', 'Owner': 'Player3'}, {'Field': 'RE2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RF1', 'Piece': 'Bishop', 'Owner': 'Player3'}, {'Field': 'RF2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RG1', 'Piece': 'Knight', 'Owner': 'Player3'}, {'Field': 'RG2', 'Piece': 'Pawn', 'Owner': 'Player3'}, {'Field': 'RH1', 'Piece': 'Rook', 'Owner': 'Player3'}, {'Field': 'RH2', 'Piece': 'Pawn', 'Owner': 'Player3'}]

'''

import random
import MESSAGE
import time

# king eat
random.seed(5311)

VALUE_PIECE = {
    "King": 1000,
    "Queen": 9,
    "Rook": 5,
    "Knight": 3,
    "Bishop": 3,
    "Pawn": 1
}

def algorithm_provider(enemy_possible_move, possible_move, current_board, type_algorithm, current_player, count_turn):
    if type_algorithm == 1:
        return play_random(possible_move)
    elif type_algorithm == 2:
        return eat_priority_first(enemy_possible_move, possible_move, current_board, current_player, count_turn)
    else:
        return play_random(possible_move)
    


def play_random(possible_move):
    while True:
        try:
            # print("This is possible move: ", possible_move)

            random_piece = random.choice(list(possible_move.keys()))
            random_move = random.choice(possible_move[random_piece])

            print(f"This is random piece: {random_piece} and random move: {random_move}")

            return random_piece, random_move
        except:
            pass

        time.sleep(0.5)

def walk_dodge(enemy_possible_move, possible_move, current_board, current_player, block_move, enemy_all_move):
    dodge_moves = []
    print(MESSAGE.TEST_DODGE)

    for my_piece, my_moves in possible_move.items():
        if my_piece in enemy_all_move:
            dodge_moves.append({
                "Field": my_piece,
                "Movable": [x for x in my_moves if x not in block_move],
                "Value": VALUE_PIECE[[x['Piece'] for x in current_board if x['Field'] == my_piece][0]],
            })

    # for enemy_piece, enemy_moves in enemy_possible_move.items():
    #     for my_piece, my_moves in possible_move.items():
    #         if my_piece in enemy_moves:
    #             dodge_moves.append({
    #                 "Field": my_piece,
    #                 "Movable": [x for x in possible_move[my_piece] if x not in block_move],
    #                 "Value": VALUE_PIECE[[x['Piece'] for x in current_board if x['Field'] == my_piece][0]],
    #             })

    # for piece, enemy_moves in enemy_possible_move.items():
    #     for enemy_move_field in enemy_moves:
    #         for board in current_board:
    #             if enemy_move_field == board['Field'] and board['Owner'] == current_player:

    #                 if board['Field'] in possible_move:
    #                     dodge_moves.append({
    #                         "Field": board['Field'],
    #                         "Movable": [x for x in possible_move[board['Field']] if x not in block_move],
    #                         "Value": VALUE_PIECE[board['Piece']],
    #                     })

    if len(dodge_moves) == 0:
        return None, None
    
    dodge_moves = sorted(dodge_moves, key=lambda x: (x['Value'], len(x['Movable'])), reverse=True)
    
    print("This is dodge moves: ", dodge_moves)

    if len(dodge_moves[0]["Movable"]) > 0:
        return dodge_moves[0]["Field"], dodge_moves[0]["Movable"][0]
    
    print('CANT DODGE accept enemy eat')
    return walk_but_dont_eat(enemy_possible_move, possible_move, current_board, current_player, False)


def walk_but_dont_eat(enemy_possible_move, possible_move, current_board, current_player, accept_eat=False):
    block_move = set(move_field for moves in enemy_possible_move.values() for move_field in moves)
    print("This is block move: ", block_move)

    enemy_all_move = []
    for enemy_moves in enemy_possible_move.values():
        enemy_all_move += enemy_moves

    if accept_eat:
        piece, random_dodge = walk_dodge(enemy_possible_move, possible_move, current_board, current_player, block_move, enemy_all_move)

        if random_dodge is not None:
            print(MESSAGE.DODGE)
            return piece, random_dodge
        
    
    
    collect_piece = []
    for my_piece, my_moves in possible_move.items():
        for move in my_moves:
            if move not in enemy_all_move:
                collect_piece.append({
                    "Piece": my_piece,
                    "Move": move,
                    "Value": VALUE_PIECE[[x['Piece'] for x in current_board if x['Field'] == my_piece][0]],
                })
    
    if len(collect_piece) == 0:
        piece_collection = []
        for my_piece, my_moves in possible_move.items():
            for move in my_moves:
                piece_collection.append({
                    "Piece": my_piece,
                    "Move": move,
                    "Value": VALUE_PIECE[[x['Piece'] for x in current_board if x['Field'] == my_piece][0]],
                })

        rd = random.choice(piece_collection)
        return rd["Piece"], rd["Move"]
                

    print("======================== THIS IS POSSIBLE MOVE DONT EAT ========================")
    print(collect_piece)

    collect_piece.sort(key=lambda x: x["Value"])

    return collect_piece[0]["Piece"], collect_piece[0]["Move"]

    # possible_move_dont_eat = {}

    # for enemy_piece, enemy_moves in enemy_possible_move.items():
    #     for my_piece, my_moves in possible_move.items():
    #         for my_move in my_moves:
    #             if my_move not in enemy_moves:
    #                 if my_piece not in possible_move_dont_eat:
    #                     possible_move_dont_eat[my_piece] = []

    #                 possible_move_dont_eat[my_piece].append(my_move)
    # print("======================== THIS IS POSSIBLE MOVE DONT EAT ========================")
    # print(possible_move_dont_eat)
    
    # return play_random(possible_move_dont_eat)
                
def is_safe_move(piece, move, current_board):
    current_piece = None
    current_move = None

    for board in current_board:
        if board['Field'] == piece:
            current_piece = board['Piece']
        
        if board['Field'] == move:
            current_move = board['Piece']

    if current_piece == "Queen" and current_move == "Pawn":
        print("CANT MOVE TO THIS PLACE")
        return True

    return False

def eat_priority_first(enemy_possible_move, possible_move, current_board, current_player, count_turn):
    current_board = current_board['Board']
    print("Calculate eat priority first")

    print(MESSAGE.ENEMY)

    max_value = 0
    max_piece = None
    max_move = None

    enemy_piece = enemy_possible_move.keys()

    for my_piece, my_moves in possible_move.items():
        for move in my_moves:
            if move in enemy_piece:
                my_piece_value = VALUE_PIECE[[x['Piece'] for x in current_board if x['Field'] == my_piece][0]]
                enemy_piece_value = VALUE_PIECE[[x['Piece'] for x in current_board if x['Field'] == move][0]]

                if enemy_piece_value == VALUE_PIECE['Pawn'] and my_piece_value == VALUE_PIECE['Queen'] and count_turn < 20:
                    print("CANT EAT PAWN")
                    continue

                if enemy_piece_value >= my_piece_value:
                    if enemy_piece_value > max_value:
                        max_value = enemy_piece_value
                        max_piece = my_piece
                        max_move = move


    if max_piece is None or max_move and None or is_safe_move(max_piece, max_move, current_board):
        return walk_but_dont_eat(enemy_possible_move, possible_move, current_board, current_player, True) # วิ่งหนี

    # compare between enemy who can eat my piece
    my_piece_enemy_eat = []

    for enemy_piece, enemy_moves in enemy_possible_move.items():
        for my_piece, my_moves in possible_move.items():
            if my_piece in enemy_moves:
                my_piece_enemy_eat.append({
                    "Piece": my_piece,
                    "Value": VALUE_PIECE[[x['Piece'] for x in current_board if x['Field'] == my_piece][0]],
                })
    
    print("This is enemy can eat: ", my_piece_enemy_eat)
    
    if len(my_piece_enemy_eat) > 0:
        for i in my_piece_enemy_eat:
            if i['Value'] > max_value:
                piece_can_move = possible_move[i['Piece']]
                enemy_all_move = []
                
                for enemy_moves in enemy_possible_move.values():
                    enemy_all_move += enemy_moves

                for move in piece_can_move:
                    if move not in enemy_all_move:
                        print(MESSAGE.ENEMY_CAN_EAT)

                        max_value = i['Value']
                        max_piece = i['Piece']
                        max_move = move

    # if enemy eat my piece and this my piece priority is high more than I can eat enemy piece, I will dodge_moves

    print(f"This is max piece: {max_piece} and max move: {max_move}")

    return max_piece, max_move