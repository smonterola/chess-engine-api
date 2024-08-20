from fastapi import FastAPI, Request, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
#from routers.items import router as item_router
#from routers.automations import router as automations_router

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import APIKEY
from accessBook import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in APIKEY.APIKEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
#app.include_router(item_router)
#app.include_router(automations_router)

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = [
    "https://localhost:3000",
    "https://chess.roastlemon.com"
    "http://localhost:3000",
    "http://chess.roastlemon.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
#@limiter.limit("1/second")
def home(
    request: Request
):
    return {"Server is live": "Success", "request":request.json}

@app.post("/engine/{fen_encoding}") #, dependencies=[Depends(api_key_auth)])
#@limiter.limit("1/second")
async def engine(
    fen_encoding: str,
    request: Request
):
    fen = fixFen(fen_encoding)
    #params = request.query_params
    #print(params)
    #print(request.query_params)
    size = lenBook()
    
    return {
        "Client host": request.client.host, 
        "bookSize" : size,
        "fen" : fen,
        "bookArg" : bookArgs(fen),
        "moves": hasBook(bookArgs(fen))
    }


