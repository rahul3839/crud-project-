from django.db import models

# Create your models here.
class RegstrationModel(models.Model):
    name = models.CharField(max_length=270)
    last_name = models.CharField(max_length=270)

    def __str__(self):
        return self.name