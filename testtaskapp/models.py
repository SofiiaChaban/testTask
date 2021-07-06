from django.db import models

class Theme(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
         return self.title