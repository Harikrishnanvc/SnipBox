from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from snippets.models import Snippets, Tag
from snippets.serializers import SnippetsSerializer, TagSerializer


class SnippetView(ModelViewSet):
    """
     Snippet API endpoints.

    - `GET /api/snippets/overview/` → Get total count & list of snippets.
    - `POST /api/snippets/` → Create a snippet.
    - `GET /api/snippets/{id}/` → Retrieve a snippet.
    - `PUT /api/snippets/{id}/` → Update a snippet.
    - `DELETE /api/snippets/{id}/` → Delete a snippet and returns the available ones.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SnippetsSerializer

    def get_queryset(self):
        return Snippets.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


