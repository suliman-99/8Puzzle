from __future__ import annotations
from typing import List
import copy
from Pos import Pos

class Puzzle:
    space = "_"
    moves = [
        Pos( 0,  1),
        Pos( 0, -1),
        Pos( 1,  0),
        Pos(-1,  0),
    ]

    @classmethod
    def find_space_pos(cls, grid: List[List[str]]) -> Pos:
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == cls.space:
                    return Pos(x, y)

    @classmethod
    def new_Puzzle(cls, grid: List[List[str]]) -> Puzzle:
        space_pos = cls.find_spaces_pos(grid)
        return cls(grid, space_pos, 0)

    def __init__(self, grid: List[List[str]], space_pos: Pos,level: int) -> Puzzle:
        self.grid = grid
        self.space_pos = space_pos
        self.level = level
        self.expected_cost = None

    def calc_expected_cost(self, end: Puzzle) -> int:
        expected_cost = 0
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if self.grid[y][x] != end.grid[y][x]:
                    expected_cost += 1
        self.expected_cost = expected_cost

    def is_valid(self, pos: Pos) -> bool:
        if 0 <= pos.y and pos.y < len(self.grid) and 0 <= pos.x and pos.x < len(self.grid[pos.y]):
            return True
        return False

    def move(self, pos: Pos) -> Puzzle:
        if self.is_valid(pos):
            temp = copy.deepcopy(self)
            temp.grid[self.space_pos.y][self.space_pos.x] = self.grid[pos.y][pos.x]
            temp.grid[pos.y][pos.x] = self.grid[self.space_pos.y][self.space_pos.x]
            temp.space_pos = pos
            temp.level += 1;
            return temp
        else:
            return None

    def generate_all_children(self) -> List[Puzzle]:
        children = []
        for new_pos in [self.space_pos + move for move in self.moves]:
            child = self.move(new_pos)
            if child is not None:
                children.append(child)
        return children


    # the same Function but this is in one line with the List Comprehensions Technique
    
    # def generate_all_children(self) -> List[Puzzle]:
    #     return [child for child in [self.move(self.space_pos + move) for move in self.moves] if child is not None]