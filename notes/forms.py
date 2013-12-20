from django import forms
from datetime import datetime

class NoteForm(forms.Form):
    noteName = forms.CharField(required = True)
    noteTags = forms.CharField()
    noteBody = forms.CharField()
    noteColor = forms.CharField()
    noteCreated = forms.DateTimeField(initial = datetime.now)
    noteEdited = forms.DateTimeField(initial = datetime.now)
