from django.urls import path
from .views import ConvertApiView


urlpatterns = [
    path('rates/', ConvertApiView.as_view(), name='api-convert'),
]