from .models import QPost
from rest_framework import serializers


class QPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QPost
        fields = ('post_title', 'post_text', 'post_author', 'post_date')