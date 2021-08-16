import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from account.managers import UserAccountManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(blank=False, null=False, max_length=100)
    last_name = models.CharField(blank=False, null=False, max_length=100)

    is_verified = models.BooleanField(default=False)
    verified = models.DateTimeField(default=None, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    last_login = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserAccountManager()

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return "/users/%i/" % self.pk
