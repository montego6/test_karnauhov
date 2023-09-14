from django.urls import path
from .views import ConvertApiView


urlpatterns = [
    path('', ConvertApiView.as_view()),
]