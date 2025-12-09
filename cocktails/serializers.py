from rest_framework import serializers
from .models import Cocktail, Source

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['name','url']

class CocktailSerializer(serializers.ModelSerializer):
    source = SourceSerializer(required=False)

    class Meta:
        model = Cocktail
        fields = ['id','title','ingredients','instructions','tags','source','source_url','metadata']
