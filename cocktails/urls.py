from django.urls import path
from .views import CocktailIngestView

urlpatterns = [
    path('', CocktailIngestView.as_view(), name='cocktail-ingest'),
]
