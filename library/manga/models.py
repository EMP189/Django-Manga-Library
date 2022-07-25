from django.db import models
from multiselectfield import MultiSelectField # this library is needed to have multiple choice option in forms

# Create your models here.
# Let's make the custom manga library
# Create the choices for the read status form, each item is a tuple with (item_key, item_value)
READ_STATUS = [
    (1,'Read later'),
    (2,'Reading'),
    (3,'Finished')
    ]
# Now create the model  
class Manga(models.Model):
    name = models.CharField(max_length=200) # name of the manga
    read_status = MultiSelectField(choices=READ_STATUS) # status of the manga ( read later/reading/finished )
    chapter = models.IntegerField(default=1) # chapter where we left it
