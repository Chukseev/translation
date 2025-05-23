from django.db import models
import os


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    description = models.TextField()
    date_translation = models.DateTimeField()
    date_added = models.DateTimeField(auto_now=True)
    src_video = models.CharField(max_length=200)
    src_donation = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text

