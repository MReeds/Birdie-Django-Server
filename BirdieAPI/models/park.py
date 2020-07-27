from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Park(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("park")
        verbose_name_plural = ("parks")
        
    def __str__(self):
        return f"{self.title}, {self.city}, {self.state}"