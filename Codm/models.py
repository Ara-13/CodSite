from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

from Codm.views import account

class CodAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    code = models.IntegerField(primary_key=True)
    pub_date = models.DateTimeField(auto_now=True)
    level = models.IntegerField(default=1)
    
    Region = (
        ('IR', 'Iran'),
        ('IN', 'India'),
        ('EU', 'Europe'),
    )

    region = models.CharField(max_length=2, choices=Region, default='IR')

    cp = models.IntegerField(default=0, blank=True, null=True)
    c = models.IntegerField(default=0, blank=True, null=True)

    multi_ranked = models.CharField(max_length=200, blank=True, null=True)
    battle_ranked = models.CharField(max_length=200, blank=True, null=True)

    battle_pass = models.TextField(max_length=900, blank=True, null=True)
    description = models.TextField(max_length=900, blank=True, null=True)

    Status = (
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('w4p', 'WairForPublish'),
    )

    status = models.CharField(max_length=10, choices=Status, default='available')

    price = models.IntegerField()

class Video(models.Model):
    account = models.OneToOneField(CodAccount, on_delete=models.CASCADE)
    #video
    #url

class Link(models.Model):
    account = models.OneToOneField(CodAccount, on_delete=models.CASCADE)
    Ts = (
        ('activision' , 'Activision'),
        ('gmail' , 'Gmail'),
        ('apple_id' , 'Apple_ID'),
        ('line' , 'Line'),
    )
    Type = models.CharField(max_length=10, choices=Ts, default="Activision")
    mail = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
