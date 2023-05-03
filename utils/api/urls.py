
from django.urls import path
from . import views

urlpatterns = [
    path('image/create/' , views.CreateImageView.as_view() , name="createImage"),
    path('image/list/' , views.ListImageView.as_view(), name='ListImages'),
    # path('image/<int:pk>/delete/' , views.DeleteImageView.as_view() , name= 'Delete_image'),
]
