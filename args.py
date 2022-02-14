from pydantic import BaseModel
from typing import List, Tuple
from enum import Enum

class Event(Enum):
    # Report beginning
    # params: ()
    NEW_GAME = 0

    # Player don't have any valid piece
    # params: (player)
    PASS = 1

    # Player makes a move
    # params: (player, piece, head)
    MOVE = 2

    # Last piece of a player is put
    # params: (player)
    FINAL = 3

    # None player has a valid piece
    # params: ()
    OVER = 4

    # Report winner
    # params: (team) team=0(First team) team=1(Second team) team=-1(Tie)
    WIN = 5

    # Player attempted an invalid move
    # params: (piece, head, player)
    INVALID = 6

    # Player step function takes too long
    # params: (player)
    TIMEOUT = 7
    
class Reset(BaseModel):
    position: int
    pieces: List[Tuple]
    max_number: int
    timeout: int
    score: Tuple[int, int]

    def __iter__(self):
        return iter([
            self.position, 
            self.pieces, 
            self.max_number,
            self.timeout,
            self.score
        ])
