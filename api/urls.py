from rest_framework import routers
from .views import GenreViewSet, CharacterViewSet, MovieViewSet

router = routers.DefaultRouter()

router.register('api/genres', GenreViewSet, 'genres')
router.register('api/characters', CharacterViewSet, 'characters')
router.register('api/movies', MovieViewSet, 'movies')

urlpatterns = router.urls

