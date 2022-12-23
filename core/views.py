from django.shortcuts import render
from django.http import HttpRequest
from .puzzle_logic.Game import Game


def home_page(request: HttpRequest):
    return render(request, "home_page.html")


def result_page(request: HttpRequest):
    data = request.POST
    game = Game.new_game(
            [
                [data['start_1'],data['start_2'],data['start_3'],],
                [data['start_4'],data['start_5'],data['start_6'],],
                [data['start_7'],data['start_8'],data['start_9'],],
            ],
            [
                [data['end_1'],data['end_2'],data['end_3'],],
                [data['end_4'],data['end_5'],data['end_6'],],
                [data['end_7'],data['end_8'],data['end_9'],],
            ],
        )
    path = game
    if isinstance(game,Game):
        path = game.get_path()
    return render(request, "result_page.html", {'path': path})