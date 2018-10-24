# QUser/serializers.py

from rest_framework import serializers
from . import models

class QUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('email','username')


