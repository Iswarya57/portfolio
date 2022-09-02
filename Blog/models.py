from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=100)


