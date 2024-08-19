from fastapi import FastAPI, Request, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import APIKEY

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

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = [
    "https://localhost:3000",
    "https://chess.roastlemon.com"
    "http://localhost:3000",
    "http://chess.roastlemon.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
@limiter.limit("1/second")
def home(
    request: Request
):
    return {"Server is live": "Success", "request":request.json}

@app.get("/engine", dependencies=[Depends(api_key_auth)])
@limiter.limit("1/second")
def engine(
    request: Request
):
    return {"Client host": request.client.host, "params": request.query_params}


