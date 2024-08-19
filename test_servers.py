import requests
import APIKEY
headers = {
    'Authorization': f'Bearer {APIKEY.APIKEYS[0]}'
}

print(requests.get(
    url="https://chess-engine-api.onrender.com", 
    headers=headers, 
    params={"fen":"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}
    ).json())

print(requests.get(
    url="http://127.0.0.1:8000/engine", 
    headers=headers, 
    params={"fen":"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}
    ).json())

print(requests.get(
    url="https://chess-api.roastlemon.com",
    headers=headers,
    ))