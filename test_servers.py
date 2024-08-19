import requests

headers = {
    'Authorization': 'Bearer cd6b569e-42cd-4f2f-9132-f6b3f0d61d40'
}
print(requests.get(
    url="http://chess-api.roastlemon.com", 
    headers=headers, 
    params={"fen":"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}
    ).json())

print(requests.get(
    url="http://127.0.0.1:8000", 
    headers=headers, 
    params={"fen":"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}
    ).json())