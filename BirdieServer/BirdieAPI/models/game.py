from django.db import models
from django.urls import reverse
from .park import Park
from .bag import Bag
from django.contrib.auth.models import User

class Game(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    park = models.ForeignKey(Park, on_delete=models.DO_NOTHING)
    bag = models.ForeignKey(Bag, on_delete=models.DO_NOTHING)
    score = models.IntegerField(null=True)
    started_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name = ("game")
        verbose_name_plural = ("games")
        
    def __str__(self):
        return f"This game was started at {self.started_at}. It was played at {self.park_id.title}. Final score was {self.score}."