import random
import time

VALUE_PIECE = {
    "King": 1000,
    "Queen": 9,
    "Rook": 5,
    "Bishop": 3,
    "Knight": 3,
    "Pawn": 1
}

def algorithm_provider(possible_move, current_board, type_algorithm):
    if type_algorithm == 1:
        return play_random(possible_move)
    elif type_algorithm == 2:
        return eat_priority_first(possible_move, current_board)
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


def eat_priority_first(possible_move, current_board):
    max_value = 0
    max_piece = None
    max_move = None

    for piece, move in possible_move.items():
        for move_field in move:
            for board in current_board:
                if move_field == board['Field']:
                    if VALUE_PIECE[board['Piece']] > max_value:
                        max_value = VALUE_PIECE[board['Piece']]
                        max_piece = piece
                        max_move = move_field
    
    if max_piece is None or max_move is None:
        return play_random(possible_move)

    print(f"This is max piece: {max_piece} and max move: {max_move}")
    return max_piece, max_move