from __future__ import annotations

class Pos:
    def __init__(self, x: int, y: int) -> Pos:
        self.x = x
        self.y = y
    
    def __add__(self, other: Pos) -> Pos:
        return Pos(self.x+other.x,self.y+other.y)