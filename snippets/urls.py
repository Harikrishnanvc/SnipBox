from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets.views import SnippetView

router = DefaultRouter()
router.register(r'snippets', SnippetView, basename='snippet')

urlpatterns = [
    path('', include(router.urls)),
]
