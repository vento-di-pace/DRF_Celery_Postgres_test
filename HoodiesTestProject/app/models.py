from django.db import models
import HoodiesTestProject.settings as settings

# Create your models here.


class Page(models.Model):
    title = models.TextField()


class Content(models.Model):
    page  = models.ForeignKey(Page, related_name='content', on_delete=models.CASCADE)
    title = models.TextField()
    counter = models.PositiveIntegerField(default=0)


class Video(models.Model):
    content = models.OneToOneField(Content, related_name='video', on_delete=models.CASCADE)
    file = models.FileField()
    subtitles = models.FileField()


class Audio(models.Model):
    content = models.OneToOneField(Content, related_name='audio', on_delete=models.CASCADE)
    file = models.FileField()
    bitrate = models.IntegerField()


class Text(models.Model):
    content = models.OneToOneField(Content, related_name='text', on_delete=models.CASCADE)
    text = models.TextField()
