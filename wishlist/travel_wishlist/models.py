from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_too='user_images/', blank=True, null=True)

    def __str__(self): #adding date_visited and photo 
        photo_str = self.photo.url if self.photo else 'no photo'
        notes_str = self.notes[100:] #truncate the first 100 characters
        return f'{self.name}, visited? {self.visited} on {self.date_visited}. Notes: {notes_str,} Photo {photo_str}'
