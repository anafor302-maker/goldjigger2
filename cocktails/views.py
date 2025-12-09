from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_api_key.permissions import HasAPIKey
from .serializers import CocktailSerializer
from .models import Source, Cocktail

class CocktailIngestView(APIView):
    permission_classes = [HasAPIKey]

    def post(self, request):
        serializer = CocktailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        src_data = data.pop('source', None)
        src = None
        if src_data:
            src, _ = Source.objects.get_or_create(name=src_data['name'], defaults={'url': src_data.get('url')})
        cocktail = Cocktail.objects.create(source=src, **data)
        # TODO: Kuyruğa iş tetikle (celery vb)
        return Response({'id': str(cocktail.id)}, status=status.HTTP_201_CREATED)
