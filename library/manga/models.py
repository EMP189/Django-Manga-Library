from django.db import models

# Create your models here.
# Let's make the custom manga library
class Manga(models.Model):
    name = models.CharField(max_length=200)
    read_status = models.BooleanField()
    chapter = models.IntegerField()
