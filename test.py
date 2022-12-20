from Game import Game

game = Game.new_game(
        [
            ["_","2","3",],
            ["1","5","6",],
            ["4","7","8",],
        ],
        [
            ["1","2","3",],
            ["4","5","6",],
            ["7","8","_",],
        ],
    )

path = game.get_path()

for grid in path:
    print(grid)




