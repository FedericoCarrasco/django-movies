from rest_framework import serializers
from .models import Genre, Character, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'image')
        read_only_fields = ('id')

