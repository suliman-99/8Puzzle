from django import template
from ..puzzle_logic.Puzzle import Puzzle

register = template.Library()

@register.filter
def is_str(value):
    return type(value) is str

@register.filter
def my_len(value):
    return len(value) - 1
    
@register.filter
def is_space(value):
    return value == Puzzle.space