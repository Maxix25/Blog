import os
from django.db.models.signals import pre_save
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

def getcurrentusername(instance, filename):
    return "static/profile_pics/{0}/{1}".format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete = models.CASCADE,
        primary_key = True
    )
    image = models.ImageField(default = "default.jpeg", upload_to = getcurrentusername)
    bio = models.CharField(max_length = 150)
    def __str__(self):
        return self.user.username





@receiver(pre_save, sender=Profile)
def delete_old_file(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered 
    if instance._state.adding and not instance.pk:
        return False
    
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    
    # comparing the new file with the old one
    file = instance.image
    if not old_file == file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)