from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_delete, post_save


def CreateProfile(sender, instance, created, **kwargs):
    if created:
        User = instance
        Profile.objects.create(
            user=User,
            username=User.username,
            name=User.first_name,
            email=User.email,
        )

def DeleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

def UserUpdate(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.email = profile.email
        user.last_name = profile.surname
        user.save()



post_save.connect(CreateProfile, sender = User)
post_save.connect(UserUpdate, sender = Profile)
# post_delete.connect(DeleteUser, sender = Profile) because breaking the user deliting 