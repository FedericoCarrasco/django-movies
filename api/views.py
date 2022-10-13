from .models import Genre, Character, Movie
from rest_framework import viewsets, permissions
from .serializers import GenreSerializer, CharacterSerializer, MovieSerializer

# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]

