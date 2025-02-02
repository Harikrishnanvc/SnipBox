from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets.views import SnippetView, TagView

router = DefaultRouter()
router.register(r'snippets', SnippetView, basename='snippet')
router.register(r'tags', TagView, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]
