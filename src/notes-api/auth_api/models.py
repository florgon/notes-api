from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    """ Auth user. """
    # TODO. IK THIS SHIT!
    # TODO. FIX ASAP!
    vk_user_id = models.TextField(null=True, blank=True, default=None, verbose_name="VK user index", help_text="VK auth service provider user index.")
