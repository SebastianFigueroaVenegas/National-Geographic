from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import MovieViewSet, ChatMessageViewSet
from catalogo import views

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'chat', ChatMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
