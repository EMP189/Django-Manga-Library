from django.db import models
# Create your models here.
# Let's make the custom manga library
# Create the choices for the read status form, each item is a tuple with (item_key, item_value)
# Now create the model  
class Manga(models.Model):
    READ_STATUS_CHOICES= [ #First value of tupple is value stored in the DB, second is the one shown in widget on the website
        ('RL','Read later'),
        ('R','Reading'),
        ('F','Finished')
        ]
    name = models.CharField(max_length=200) # name of the manga
    read_status = models.CharField(max_length=15,
                                choices=READ_STATUS_CHOICES,
                                default='Read later')
    chapter = models.IntegerField(default=1) # chapter where we left it
