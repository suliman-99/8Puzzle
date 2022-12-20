from __future__ import annotations
from typing import List
from Puzzle import Puzzle
from queue import PriorityQueue


class Game:
    @classmethod
    def new_game(cls, start: List[List[str]], end: List[List[str]]) -> Game:
        start_puz = Puzzle.new_puzzle(start)
        end_puz = Puzzle.new_puzzle(end)
        if start_puz is None or end_puz is None: return None
        if start_puz.clac_grid_diferences(end_puz) == -1: return None
        return cls(start_puz, end_puz)


    def __init__(self, start: Puzzle, end: Puzzle) -> Game:
        self.start = start
        self.end = end
        self.path = []
        self.solved = False

    def get_path(self) -> List[Puzzle]:
        if not self.path and not self.solved: 
            self.calc_path()
        return self.path

    def calc_path(self) -> None:
        end = self.a_star()
        while end is not None:
            self.path.append(end)
            end = end.father
        self.path.reverse()
        self.solved = True

    def a_star(self) -> Puzzle:
        open: PriorityQueue[tuple[int ,Puzzle]] = PriorityQueue()
        closed: List[Puzzle] = []

        val = self.start.calc_expected_cost(self.end)
        open.put((val,self.start))
        closed.append(self.start)

        while(not open.empty()):
            _, top = open.get()
            if top.clac_grid_diferences(self.end) == 0:
                return top
            for child in top.get_all_children():
                is_new = True
                for c in closed:
                    if c == child:
                        is_new = False
                        break
                if is_new:
                    val = child.calc_expected_cost(self.end)
                    open.put((val, child))
                    closed.append(child)
        return None



