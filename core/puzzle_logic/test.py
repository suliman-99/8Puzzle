from .Game import Game

game = Game.new_game(
        [
            ["4","1","2",],
            ["7","5","3",],
            ["8","_","6",],
        ],
        [
            ["1","2","3",],
            ["4","5","6",],
            ["7","8","_",],
        ],
    )

if not isinstance(game,Game):
    print(game)
else:
    path = game.get_path()
    for grid in path:
        print(grid)



