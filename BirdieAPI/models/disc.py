from django.db import models
from django.urls import reverse
from .bag import Bag
from django.contrib.auth.models import User
from django.utils.translation import gettext

class Disc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(null=True, max_length=20)
    name = models.CharField(null=True, max_length=20)
    disc_type = models.CharField(null=False, max_length=15)
    bag = models.ForeignKey(Bag, null=True, on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=20, null=True)
    speed = models.IntegerField(null=True)
    glide = models.IntegerField(null=True)
    turn = models.IntegerField(null=True)
    fade = models.IntegerField(null=True) 

    class Meta:
        verbose_name = ("disc")
        verbose_name_plural = ("discs")
        
    def __str__(self):
        return self.disc_type