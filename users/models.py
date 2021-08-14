from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, )
    cards = models.TextField(null=True, blank=True, default="")
    col_rel= models.TextField(null=True, blank=True, default="")
    utilits = models.TextField(null=True, blank=True, default="")
    links = models.TextField(null=True, blank=True, default="")


# Create your models here.
