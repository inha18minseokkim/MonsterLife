from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from Filter import Filter
import asyncio
import nest_asyncio
from urllib.parse import unquote
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
nest_asyncio.apply()
@app.get("/")
async def root():
    return {"message": "Hello World"}

templates = Jinja2Templates(directory='Page')
@app.get("/monster")
async def say_hello(arg: str):
    return templates.TemplateResponse("main.html")

@app.get("/getfarmlist/{arg}")
async def say_hello(arg: str):
    arg = unquote(arg)
    print(arg.split(','))
    res = asyncio.run(Filter(arg.split(',')))
    print(res)
    return JSONResponse({'data': res})
