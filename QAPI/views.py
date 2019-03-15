from django.utils import timezone
from rest_framework import viewsets

from .models import QPost
from .serializers import QPostSerializer


# Create your views here.
class QPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = QPost.objects.all()
    serializer_class = QPostSerializer

    def perform_create(self, serializer):
        serializer.save(post_id=self.request.POST.get("post_id"),
                        post_title=self.request.POST.get("post_title"),
                        post_text=self.request.POST.get("post_text"),
                        post_author=self.request.POST.get("post_author"),
                        post_date=timezone.now())
