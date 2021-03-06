""" Models ued to handle the user of the app"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    """ Based on the user model, we extend it with new info"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nb_adv_played = models.IntegerField(blank=True)
    nb_adv_created = models.IntegerField(blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created):
    """ We make sure that wen we create a user, we create a profile as well"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance):
    """ We make sure that wen we update a user, we update the profile as well"""
    instance.profile.save()
