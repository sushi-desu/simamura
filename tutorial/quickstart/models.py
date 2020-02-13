from django.db import models

# Create your models here.
class Quick(models.Model):
  name = models.CharField(max_length=250)
  number = models.IntegerField(default=0)
