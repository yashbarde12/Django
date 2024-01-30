from django.db import models

# Create your models here.

class MediaManager(models.Manager):
    def audio(self):
        return self.filter(type='Audio')

    def video(self):
        return self.filter(type='Video')

    def images(self):
        return self.filter(type='Image')

class Media(models.Model):
    TYPE_CHOICES = (
        ('Audio', 'Audio'),
        ('Video', 'Video'),
        ('Image', 'Image'),
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    format = models.CharField(max_length=10)
    size = models.IntegerField()  
    duration_secs = models.IntegerField(default=0)

    objects = MediaManager()

    def __str__(self):
        return f"{self.name} - {self.type}"
