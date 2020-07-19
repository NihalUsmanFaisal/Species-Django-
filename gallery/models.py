from django.db import models
from datetime import datetime

# Create your models here.
class Images(models.Model):
    img = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=datetime.now)
    animal = models.CharField(max_length=100)
    def __str__(self):
        return self.animal
