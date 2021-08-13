from django.http import FileResponse
from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import ImageSerializer
from .models import Image


# create method was provided automatically
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    # load the last created object
    @action(methods=['get'], detail=False)
    def download(self, *args, **kwargs):
        # get the last created object
        instance = self.get_queryset().last()
        try:
            file_handle = instance.upload.open()
            response = FileResponse(file_handle, content_type='whatever')
            response['Content-Length'] = instance.upload.size
            response['Content-Disposition'] = 'attachment; filename="%s"' % instance.upload.name
            return response
        # catch nonetype and file existence exceptions 
        except (AttributeError, FileNotFoundError):
            raise Http404
