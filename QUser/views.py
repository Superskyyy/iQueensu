# ListCreateAPI view

from rest_framework import generics
from . import models
from . import serializers

class QUserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.QUserSerializer
