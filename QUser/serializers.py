# QUser/serializers.py

from rest_framework import serializers

from . import models
from django.contrib.auth.models import AbstractUser


class QUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbstractUser
        fields = ('email', 'username', 'first_name', 'last_name')
