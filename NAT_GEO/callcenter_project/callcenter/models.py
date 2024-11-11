from django.db import models
from django.contrib.auth.models import User
from django.db import models

class AdminAction(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)