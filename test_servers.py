import requests
import src.APIKEY as APIKEY
from src.accessBook import fixFen
headers = {
    'Authorization': f'Bearer {APIKEY.APIKEYS[0]}'
}

starting_board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
d4_fen = "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1"
encoded_fen = fixFen(starting_board)

'''
#TESTING MY DOMAIN
print(requests.get(
    url=f"https://chess-api.roastlemon.com/engine/{encoded_fen}", 
    headers=headers, 
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
    headers=headers, 
    ).json())
url = f"http://127.0.0.1:8000/engine/{fixFen(d4_fen)}"
print(requests.get(
    url=url,
    headers=headers, 
    ).json())
url = f"http://127.0.0.1:8000/engine/NA{encoded_fen}"
print(requests.get(
    url=url,
    headers=headers, 
    ).json())
