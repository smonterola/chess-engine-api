import requests
import APIKEY
from accessBook import fixFen
headers = {
    'Authorization': f'Bearer {APIKEY.APIKEYS[0]}'
}

starting_board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
encoded_fen = fixFen(starting_board)
#TESTING MY DOMAIN
'''
print(requests.get(
    url="https://chess-api.roastlemon.com/engine", 
    headers=headers, 
    params={"fen":"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}
    ).json())

print(requests.get(
    url="https://chess-api.roastlemon.com/engine", 
    headers=headers, 
    params={"fen":"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}
    ).json())
'''
    

#TESTING LOCAL VERSION / DEVELOPMENT
print(requests.get(
    url="http://127.0.0.1:8000", 
    headers=headers, 
    ).json())

url = f"http://127.0.0.1:8000/engine/{encoded_fen}"
print(requests.get(
    url=url,
    json={"test":"test"},
    headers=headers, 
    ).json())

