from rest_framework import viewsets
from rest_framework.decorators import action

from buildup.models import Unit
from core.utils import from_xlsx_to_csv_to_bd, download_csv_to_xlsx
from .permissions import IsAuthorPermission
from .serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthorPermission]

    @action(methods=('post',), detail=True)
    def perform_create(self, serializer):
        author = self.request.user.id
        from_xlsx_to_csv_to_bd(author)
        serializer.save(author=self.request.user)

    @action(methods=('get',), detail=False)
    def download_and_get(self, request, *args, **kwargs):
        if request.method == 'GET':
            return (download_csv_to_xlsx(request))
