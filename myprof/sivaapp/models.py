from django.db import models


class Data (models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256,default="None")
    text=models.CharField(max_length=512,default="None")
    
    def __str__(self):
        return self.name