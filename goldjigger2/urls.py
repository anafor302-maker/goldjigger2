from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from cocktails.views import create_superuser


def home(request):
    return JsonResponse({"message": "API running!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("create-superuser/", create_superuser),
    path('api/v1/cocktails/', include('cocktails.urls')),
]
