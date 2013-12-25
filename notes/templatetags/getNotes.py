from django import template
import os, os.path

register = template.Library()


@register.filter
def getNoteBody(noteLocation):
    if os.getcwd()[-7::] != "library":
        os.chdir("library")
    location = noteLocation
    f = open(location, "r")
    noteBody = f.read()
    f.close()
    os.chdir('..')
    return noteBody

@register.filter
def returnPosList(x):
    return ["top", "left", "bottom", "right"]