import random
import MESSAGE
import time

VALUE_PIECE = {
    "King": 1000,
    "Queen": 9,
    "Rook": 5,
    "Bishop": 3,
    "Knight": 3,
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

def walk_but_dont_eat(enemy_possible_move, possible_move, current_board, current_player):
    block_move = []
    for piece, move in enemy_possible_move.items():
        for move_field in move:
            block_move.append(move_field)
    
    print("This is block move: ", block_move)
    
    min_value = 1000
    min_piece = None
    min_move = None

    for piece, move in possible_move.items():
        for move_field in move:
            if move_field not in block_move:
                for board in current_board:
                    if VALUE_PIECE[board['Piece']] < min_value:
                        min_value = VALUE_PIECE[board['Piece']]
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

    # hadle if enemy can eat my piece

    # for piece, move in enemy_possible_move.items():
    #     for move_field in move:
    #         for board in current_board:
    #             if move_field == board['Field']:
    #                 if board['Owner'] == current_player:
    #                     possible_move[piece].remove(move_field)

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

    return max_piece, max_move