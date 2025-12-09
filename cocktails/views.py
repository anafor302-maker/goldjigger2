from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import os
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
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


@api_view(["POST"])
def create_superuser(request):
    User = get_user_model()

    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")

    if User.objects.filter(username=username).exists():
        return Response({"detail": "Superuser zaten var."}, status=status.HTTP_200_OK)

    User.objects.create_superuser(username=username, email=email, password=password)

    return Response({"detail": "Superuser oluşturuldu!"}, status=status.HTTP_201_CREATED)