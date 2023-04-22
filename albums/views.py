from .models import Album
from .serializers import AlbumSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView


class AlbumView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    pagination_class = PageNumberPagination
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializer: AlbumSerializer):
        serializer.save(user=self.request.user)