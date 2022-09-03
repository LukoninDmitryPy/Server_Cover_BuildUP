from rest_framework import viewsets

from buildup.models import Unit
from .serializers import FileSerializer
from .permissions import IsAuthorOrReadOnlyPermission

# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)