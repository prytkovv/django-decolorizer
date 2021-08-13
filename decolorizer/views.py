from django.http import FileResponse
from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import ImageSerializer
from .models import Image


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    # get last created object
    def get_object(self):
        return self.get_queryset().last()

    # load the last created object
    @action(methods=['get'], detail=False)
    def download(self, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            raise Http404
        file_handle = instance.upload.open()
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.upload.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.upload.name
        return response
