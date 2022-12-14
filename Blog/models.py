from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    
    def summary(self):
        return self.body[:100]

    def date_pretty(self):
        return self.date.strftime('%b %e %Y')

    def __str__(self):
        return self.title


