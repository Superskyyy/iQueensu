from rest_framework import serializers

from .models import QPost


class QPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QPost
        fields = ('post_id', 'post_title', 'post_text', 'post_author', 'post_date')
