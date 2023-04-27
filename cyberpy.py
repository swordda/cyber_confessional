import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from slowapi.middleware import SlowAPIMiddleware
from starlette.middleware.cors import CORSMiddleware
import sql_check
from fastapi.requests import Request
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
import contral_datebase

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    text: str


@app.post("/das/cyber")
@limiter.limit("5/minute")
async def cyber(request: Request, json_data: dict):
    print(json_data)
    if json_data['content'] == '':
        return {'message': '345'}
    else:
        if (json_data['if_share'] == 'True') | (json_data['if_share'] == 'False'):
            if sql_check.check(json_data['content'], json_data['title'], json_data['contact']):
                contral_datebase.write_in_datebase(json_data['title'], json_data['content'], json_data['if_share'],
                                                   json_data['contact'])
                return {'message': '123'}
            else:
                return {'message': '234'}
        else:
            return {'message': '456'}


@app.get("/login")
def login(text: Item):
    return "0"


if __name__ == "__main__":
    uvicorn.run(app, port=2596, host="127.0.0.1")
