import requests

print(requests.get("http://chess-api.roastlemon.com/about").json())

print(requests.get("http://127.0.0.1:8000").json())