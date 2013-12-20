from django.db import models
import datetime

# Create your models here.

class Note(models.Model):
    note_id = models.IntegerField(primary_key = True)
    noteName = models.CharField(max_length = 128)
    noteLocation = models.CharField(max_length = 128)
    noteTags = models.CharField(max_length = 128)
    noteColor = models.CharField(max_length = 8)
    noteCreated = models.DateTimeField()
    noteEdited = models.DateTimeField()


class File(models.Model):
    note = models.ForeignKey(Note)
    fileLocation = models.CharField(max_length = 128)
    identifier = models.CharField(max_length = 20) #only a few options, "note", or a filename that was within the note

