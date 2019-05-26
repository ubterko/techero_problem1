from django.db import models
#from . import views

# Create your models here.
class Bvn(models.Model):
    bvnumber = models.CharField(max_length=20)
    
    def __str__(self):
        return self.bvnumber

