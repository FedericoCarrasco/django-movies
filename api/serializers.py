from rest_framework import serializers
from .models import Genre, Character, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'image')
        read_only_fields = ('id')

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name', 'image', 'age', 'weight', 'story')
        read_only_fields = ('id')

