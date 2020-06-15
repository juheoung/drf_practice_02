from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import CardViewSet

router = SimpleRouter()
router.register(r'card', CardViewSet)
urlpatterns = router.urls
