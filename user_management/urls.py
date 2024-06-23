from rest_framework import routers
from .views import MeViewSet

router = routers.DefaultRouter()
router.register('me', MeViewSet, basename='me')
