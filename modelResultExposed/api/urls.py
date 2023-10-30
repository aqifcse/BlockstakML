from django.urls import path
from .viewsets import MLModelOutputAPIView

urlpatterns = [
    path("ml-model-output/", MLModelOutputAPIView.as_view(), name="ml_model_output"),
]