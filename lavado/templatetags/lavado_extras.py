from django import template


def subtract(value, arg):
    return value - arg

register = template.Library()
register.filter('subtract', subtract)