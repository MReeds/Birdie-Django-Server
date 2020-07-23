from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Message(models.Model):
    creator = models.ForeignKey(User, related_name='sender', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(User, related_name='reciever' ,on_delete=models.DO_NOTHING)
    content = models.CharField(null=False, max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField()
    
    class Meta:
        verbose_name = ("message")
        verbose_name_plural = ("messages")
        
    def __str__(self):
        return self.content