from django.urls import path
from category.api import views

urlpatterns = [
    path('category/', views.CategoryView.as_view()),
    path('brand/', views.BrandView.as_view()),
]