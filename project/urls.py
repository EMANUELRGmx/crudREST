from rest_framework import routers
from .api import ProductoViewSet


router = routers.DefaultRouter()
router.register('api/projects', ProductoViewSet,'projects')

urlpatterns = router.urls