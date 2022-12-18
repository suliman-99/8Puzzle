import Node

class Puzzle:
    def init(self, size):
        # Initialize the puzzle size by the the specified size,open and closed lists to empty
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        # Accepts the puzzle from the user
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal):
        # Heuristic function to calculate Heuristic value f(x) = h(x) + g(x)
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        # Calculates the difference between the given puzzles
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
            # Accept Start and Goal Puzzle state
            print("enter the start state matrix \n")
            start = self.accept()
            print("enter the goal state matrix \n")
            goal = self.accept()
            start = Node(start, 0, 0)
            start.fval = self.f(start, goal)
            # put the start node in the open list
            self.open.append(start)
            print("\n\n")
            while True:
                b = False
                cur = self.open[0]
                print("==================================================\n")
                for i in cur.data:
                    for j in i:
                        print(j, end=" ")
                    print("")
                # if the difference between current and goal node is 0 we have reached the goal node
                if (self.h(cur.data, goal) == 0):
                    break
                for i in cur.generate_child():
                    i.fval = self.f(i, goal)
                    self.open.append(i)
                self.closed.append(cur)
                del self.open[0]
                # sort the open list based on f value
                self.open.sort(key=lambda x: x.fval, reverse=False)


puz = Puzzle(3)
puz.process()