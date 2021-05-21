from django.db import models
class Journal(models.Model):
    text = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)

