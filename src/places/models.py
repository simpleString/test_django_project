from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    title = models.CharField(max_length=20, verbose_name='Title')
    description = models.CharField(max_length=500, verbose_name='Description')
    # latitude = models.P(max_length=10, verbose_name='Place')
    image = models.ImageField(upload_to='place_image', verbose_name='Place image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
