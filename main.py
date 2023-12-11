import json
import websockets
import random
import asyncio
import time

class Trichess:
    def __init__(self, uri):
        self.uri = uri
        self.ebsocket = None
        self.Password = None
        self.Player = None
        self.Board = None

    async def receive_response(self):
        response = await self.websocket.recv()
        response = response.replace("True", 'true')
        response = response.replace("False", 'false')

        try:
            json_response = json.loads(response)
        except json.JSONDecodeError:
            print(f'Received non-JSON response: {response} unable to extract json.')

        return json_response

    async def connect(self):
        self.websocket = await websockets.connect(self.uri)
        player_data = await self.receive_response()
        self.Password = player_data['Password']
        self.player = player_data['Player']
        print(f'Password: {self.Password}, Player: {self.Player}')
    
    async def move_able(self, piece_field):
        data = {
            "Command": "Movable",
            "Password": self.Password,
            "Field": piece_field
        }
        await self.websocket.send(json.dumps(data))

    async def send_move(self, piece_field_from, piece_field_to):
        data = {
            "Command": "Move",
            "Password": self.Password,
            "Move": {
                "From": piece_field_from,
                "To": piece_field_to,
            }
        }
        await self.websocket.send(json.dumps(data))

    def reconnecting_game(self):
        pass

    def pass_turn(self):
        pass

    def check_king(self):
        pass

    async def myPiece(self):
        data = {
            "Command": "MyPiece",
            "Password": self.Password
        }
        await self.websocket.send(json.dumps(data))

    def promote(self):
        pass

    async def check_turn(self):
        data = {
            "Command": "CheckTurn",
            "Password": self.Password,
        }
        await self.websocket.send(json.dumps(data))

"""
"Board": [
    { "Field": "BA1", "Piece": "Rook", "Owner": "Player1" },
]
"""
def filter_own_piece(board, player):
    for piece in board:
        if piece['Owner'] != player:
            board.remove(piece)
    
    return board

async def main(url):
    trichess = Trichess(url)
    await trichess.connect()

    # loop wait to connect to game
    while True:
        try:
            game_start = await trichess.receive_response()
            print("Game", game_start)
            if game_start['Status'] != "Success":
                break
        except:
            pass

        time.sleep(1)
    
    # loop wait my turn
    while True:
        try:
            await trichess.check_turn()
            turn_response = await trichess.receive_response()
            if turn_response['Status'] != "Success":
                if turn_response['YourTurn']:
                    print(f"{'='*10}This is my turn!!!!{'='*10}")

                    trichess.Board = filter_own_piece(turn_response['Board'], trichess.Player)
                    print(f"This is my piece: {trichess.Board}")
        except:
            pass

        time.sleep(1)

if __name__ == '__main__':
    URL = 'ws://192.168.1.100:8181/game'
    # URL = input("Enter URL: ")
    asyncio.run(main(URL))