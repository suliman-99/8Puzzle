from django import template

register = template.Library()

@register.filter
def is_str(value):
    return type(value) is str

    
@register.filter
def my_len(value):
    return len(value) - 1