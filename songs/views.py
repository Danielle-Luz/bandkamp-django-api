from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView
from albums.models import Album 


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    pagination_class = PageNumberPagination
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        album_id = self.kwargs.get("pk")
        return Song.objects.filter(album_id=album_id)

    def perform_create(self, serializer):
        album_id = self.kwargs.get("pk")
        related_album = Album.objects.get(id=album_id)

        serializer.save(album=related_album)