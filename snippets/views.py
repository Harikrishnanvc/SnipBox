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

    @action(detail=False, methods=['get'])
    def overview(self, request):
        """ Returns all snippets details with total snippet count """

        snippets = Snippets.objects.filter(user=self.request.user)
        serialized_snippets = SnippetsSerializer(snippets, many=True).data
        response_data = {
            "total_snippets": snippets.count(),
            "snippets": serialized_snippets
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        snippet_ids = request.data.get('ids', [])
        user = self.request.user
        snippets = Snippets.objects.filter(user=user, id__in=snippet_ids)

        if not snippets.exists():
            return Response({"detail": "No matching snippets found."}, status=status.HTTP_404_NOT_FOUND)

        snippets.delete()

        updated_snippets = Snippets.objects.filter(user=user)
        serialized_snippets = SnippetsSerializer(updated_snippets, many=True).data
        response_data = {
            "total_snippets": updated_snippets.count(),
            "snippets": serialized_snippets
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class TagView(ReadOnlyModelViewSet):
    """
    Tag API endpoints.

    - `GET /api/tags/` → List all tags.
    - `GET /api/tags/{id}/` → Get tag details.
    - `GET /api/tags/{id}/snippets/` → Get snippets linked to a tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(detail=True, methods=['get'])
    def snippets(self, request, pk=None):
        """ Returns all snippets linked to specific tag """

        tag = self.get_object()
        snippets = Snippets.objects.filter(tags=tag).prefetch_related('tags')
        serialized_snippets = SnippetsSerializer(snippets, many=True).data
        response_data = {
            "snippets": serialized_snippets
        }
        return Response(response_data, status=status.HTTP_200_OK)
