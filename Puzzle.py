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
        space_pos = None
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == cls.space:
                    if space_pos: return None
                    space_pos = Pos(x, y)
        return space_pos

    @classmethod
    def new_puzzle(cls, grid: List[List[str]]) -> Puzzle:
        space_pos = cls.find_space_pos(grid)
        if space_pos is None: return None
        return cls(grid, space_pos, 0)

    def __init__(self, grid: List[List[str]], space_pos: Pos,level: int) -> Puzzle:
        self.grid = grid
        self.space_pos = space_pos
        self.level = level
        self.father = None

    def is_same_elements(self, other: Puzzle) -> bool:
        if len(self.grid) != len(other.grid): return False
        for y, row in enumerate(self.grid):
            if len(self.grid[y]) != len(other.grid[y]): return False
        m1 = {}
        m2 = {}
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                c1 = 0; c2 = 0
                if self.grid[y][x] in m1:
                    c1 = m1[self.grid[y][x]]
                if other.grid[y][x] in m2:
                    c2 = m2[other.grid[y][x]]
                m1[self.grid[y][x]] = c1 + 1
                m2[other.grid[y][x]] = c2 + 1
        for k in m1.keys():
            if not k in m2 :
                return False
            if m1[k] != m2[k]:
                return False
        for k in m2.keys():
            if not k in m1:
                return False
            if m1[k] != m2[k]:
                return False
        return True

    def clac_grid_diferences(self, other: Puzzle) -> int:
        diff = 0
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if self.grid[y][x] != other.grid[y][x]:
                    diff += 1
        return diff

    def calc_expected_cost(self, end: Puzzle) -> int:
        return self.level + self.clac_grid_diferences(end)

    def is_finished(self, end: Puzzle) -> bool:
        return not self.clac_grid_diferences(end)

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
            temp.father = self
            return temp
        else:
            return None

    def get_all_children(self) -> List[Puzzle]:
        children = []
        for new_pos in [self.space_pos + move for move in self.moves]:
            child = self.move(new_pos)
            if child is not None:
                children.append(child)
        return children


    # the same Function but this is in one line with the List Comprehensions Technique
    
    # def generate_all_children(self) -> List[Puzzle]:
    #     return [child for child in [self.move(self.space_pos + move) for move in self.moves] if child is not None]

    def __eq__(self, other: Puzzle) -> bool:
        if self.level > other.level: return False
        if self.space_pos != other.space_pos: return False
        if self.clac_grid_diferences(other) != 0: return False
        return True

    def __lt__(self, other: Puzzle) -> bool:
        return True

    def __le__(self, other: Puzzle) -> bool:
        return True

    def __str__(self):
        ret = ""
        for row in self.grid:
            for cell in row:
                ret += cell + " "
            ret += "\n"
        ret += "\n"
        return ret