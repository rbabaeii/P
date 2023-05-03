from django.urls import path, include
from . import views

app_name = 'Product'

urlpatterns = [
    path('list-active/',  views.ListActiveProductsView.as_view() , name = 'active-products'),
    path('list-all/',  views.ListAllProductsView.as_view() , name = 'all-products'),
    path('create/' , views.CreateProductView.as_view() , name = "create"),
    path('detail/<str:pk>/' , views.DetailProductView.as_view() , name = "detail"),
    path('user/active-products/' , views.ListUserActiveProducts.as_view()),
    path('user/waiting-products/' , views.ListUserWaitingProducts.as_view()),
    path('image/create/' , views.CreateProductImage.as_view() ),
    path('image/list/<str:pk>/' , views.ListProductImage.as_view())
]