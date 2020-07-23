from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Bag(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(null=True, max_length=25)
    
    class Meta:
        verbose_name = ('bag')
        verbose_name_plural = ('bags')