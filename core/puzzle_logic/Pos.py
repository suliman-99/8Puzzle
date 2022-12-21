from __future__ import annotations

class Pos:
    def __init__(self, x: int, y: int) -> Pos:
        self.x = x
        self.y = y
    
    def __add__(self, other: Pos) -> Pos:
        return Pos(self.x+other.x,self.y+other.y)

    def __eq__(self, other: Pos) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Pos) -> bool:
        return self.x != other.x or self.y != other.y