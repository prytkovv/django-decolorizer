from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('images', views.ImageViewSet, basename='images')
urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
