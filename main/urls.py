from django.urls import path
from .views import ConvertApiView
from django.views.generic import TemplateView


urlpatterns = [
    path("rates/", ConvertApiView.as_view(), name="api-convert"),
    path(
        "docs/",
        TemplateView.as_view(template_name="swagger-ui.html"),
        name="swagger-ui",
    ),
]
