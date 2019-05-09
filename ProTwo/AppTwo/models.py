from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    email = models.EmailField(max_length = 256, unique = True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

# Create your models here.
