# to create a profile model whenever a user is created

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .profile_model import Profile


@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
    # instance is the object or the user that is created
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save(sender, instance, **kwargs):
    instance.profile.save()
