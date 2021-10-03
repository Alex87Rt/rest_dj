from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True)

class UserModelSerializerVer1(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')