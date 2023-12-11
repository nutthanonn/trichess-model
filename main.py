import json
import websockets
import random
import asyncio
import time

class Game:
    def __init__(self, uri):
        self.uri = uri
        self.websocket = None
        self.password = None

    async def connect(self):
        self.websocket = await websockets.connect(self.uri)
        response = await self.websocket.recv()
        print(f'Response from server: {response}')

        try:
            json_response = json.loads(response)
            self.password = json_response['Password']
            print(f'Password received from server: {self.password}')

        except json.JSONDecodeError:
            print('Received non-JSON response, unable to extract json.')

    def auto_move(self):
        return f"{random.choice(['B', 'G', 'R'])}{random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])}{random.choice(['1', '2', '3', '4'])}", f"{random.choice(['B', 'G', 'R'])}{random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])}{random.choice(['1', '2', '3', '4'])}"

    async def send_move(self, piece_field_from, piece_field_to):
        data = {
            "Command": "Move",
            "Password": self.password,
            "Move": {
                "From": piece_field_from,
                "To": piece_field_to
            }
        }
        
        await self.websocket.send(json.dumps(data))

    async def receive_response(self):
        response = await self.websocket.recv()
        response = response.replace("True", 'true')

        try:
            json_response = json.loads(response)
        except json.JSONDecodeError:
            print(f'Received non-JSON response: {response} unable to extract json.')

        return json_response

    def reconnecting_game(self):
        pass

    def pass_turn(self):
        pass

    def check_king(self):
        pass

    async def myPiece(self):
        data = {
            "Command": "MyPiece",
            "Password": self.password
        }

        await self.websocket.send(json.dumps(data))

    def promote(self):
        pass

    async def check_turn(self):
        data = {
            "Command": "CheckTurn",
            "Password": self.password,
        }
        await self.websocket.send(json.dumps(data))

    def solver(self, board):
        pass

async def main(url):
    game = Game(url)
    await game.connect()

    # loop wait to connect to game
    while True:
        try:
            game_start = await game.receive_response()
            print("Game", game_start, game_start['Status'])
            if game_start['Status'] != "Success":
                break
        except:
            pass

        time.sleep(1)
    
    # loop wait my turn
    while True:
        try:
            await game.check_turn()
            turn_response = await game.receive_response()
            print("TURN", turn_response)
            if turn_response['Status'] != "Success":
                print(f"This is turn message: {turn_response}")
        except:
            pass

        time.sleep(1)

if __name__ == '__main__':
    URL = 'ws://192.168.1.100:8181/game'
    # URL = input("Enter URL: ")
    asyncio.run(main(URL))