"""
Copyright © 2022 2kodevs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
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
