from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        username = f'{instance.fisrt_name}'.lower()
        counter = 1
        while User.objects.filter(username=username):
            username = f'{instance.fisrt_name}_{counter}'
            counter += 1
        instance.username = username