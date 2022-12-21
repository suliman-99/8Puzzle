from django.shortcuts import render
from .puzzle_logic.Game import Game



def home_page(request):
    return render(request, "home_page.html")


def result_page(request):
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
    path = game
    if isinstance(game,Game):
        path = game.get_path()
    return render(request, "result_page.html", {'path': path})