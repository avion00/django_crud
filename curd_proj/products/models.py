from django.db import models

# Create your models here.

class Image(models.Model):
    photo = models.ImageField(upload_to="myImage")
    date = models.DateTimeField(auto_now_add=True)
    # name = models.CharField(max_length=50)
    # price = models.IntegerField()
    # dis = models.CharField(max_length=100)
