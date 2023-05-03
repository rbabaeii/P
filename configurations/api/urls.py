from django.urls import path
from configurations.api import views

urlpatterns = [
    path('configuration/', views.ConfigurationView.as_view()),
]