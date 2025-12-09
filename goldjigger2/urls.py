from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def home(request):
    return JsonResponse({"message": "API running!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/v1/cocktails/', include('cocktails.urls')),
]
