from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from notes.forms import NoteForm
from notes.models import Note
import os, os.path
from datetime import datetime

# Create your views here.

def test(request, *args, **kwargs):
    #A test case function to make sure urls work
    if len(args) > 0:
        return HttpResponse("This is what you said: {0}".format(args))
    else:
        return HttpResponse("This is a test page!")

def add_note(request):
    #
    return render(request, "add_note.html", {"note": NoteForm})
    """###################################################################
    
    ###################################################################"""

def note_info(request, note_id):
    #
    #note = Note.findNote(note_id)
    return HttpResponse("You're looking at note number {0}".format(note_id))

def all_notes(request):
    #
    return HttpResponse("This is all of your notes")

def createNewNote(request):
    if request.method == "POST":
        noteId = getNoteId()
        location = makeNoteLocation(request.POST['noteBody'], noteId)
        tags = splitNoteTags(request.POST["noteTags"])
        mynote = Note(note_id = noteId, noteName = request.POST["noteName"], noteLocation = location, noteTags = tags, noteColor = request.POST["noteTags"], noteCreated = datetime.now(), noteEdited = datetime.now())
        print mynote.note_id
        print mynote.noteName
        print mynote.noteLocation
        print mynote.noteTags
        print mynote.noteColor
        print mynote.noteCreated
        print str(os.getcwd())[-7::]
        mynote.save()
        return HttpResponse("You saved a note!")
    else:
        return HttpResponse("Nope!")
    
def splitNoteTags(tagString):
    return tagString

def makeNoteLocation(body, noteId):
    sep = os.sep
    if os.getcwd()[-7::] != "library":
        os.chdir("library")
    location = str(noteId)+"_"+"0.txt"
    f = open(location, "w")
    f.write(body)
    f.close()
    return location


def getNoteId():
    note = Note
    totalNotes = len(note.objects.all())
    print totalNotes
    return totalNotes + 1

