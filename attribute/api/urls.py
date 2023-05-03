from django.urls import path
from attribute.api import views

urlpatterns = [
    path('AttributeGroup/<str:pk>/', views.AttributeGroupView.as_view()),
    path('Attribute/<str:pk>/', views.AttributeView.as_view()),
    path('AttributeItem/<str:pk>/', views.AttributeItemView.as_view()),
    path('ProductAttribute/attrs/<str:pk>/', views.ProductAttributeView.as_view()),
    path('ProductAttribute/create/',views.CreateProductAttributeView.as_view()),

]