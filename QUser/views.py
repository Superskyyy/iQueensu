# ListCreateAPI view

from rest_framework import viewsets
from django.contrib.auth.models import AbstractUser
from QUser.serializers import QUserSerializer


class QUserListView(viewsets.ModelViewSet):
    queryset = AbstractUser.CustomUser.objects.all()
    serializer_class = QUserSerializer.QUserSerializer
