from django.urls import path
from .views import predict_range

urlpatterns = [
    path('', predict_range, name='predict_range'),
]