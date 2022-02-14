from simple import Random
from typing import Tuple
from fastapi import FastAPI
import args as arguments

app = FastAPI()
player = Random("foo")

@app.post("/start")
def start():
    return player.start()

@app.post("/reset")
def reset(args: arguments.Reset):
    player.reset(*args)
    
@app.post("/log")
def log(log: Tuple):
    event, *args = log
    player.log((arguments.Event(event), *args))

@app.post("/step")
def step(heads: Tuple[int, int]):
    return player.step(heads)
    