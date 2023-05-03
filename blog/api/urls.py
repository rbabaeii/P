from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('list/' ,  views.ListActiveBlogView.as_view() , name = 'list-active') ,
    path('detail/<str:slug>/' , views.RetriveUpdateDestroyBlogView.as_view()) ,
    path('<str:pk>/comments/' , views.ListCommentView.as_view()) ,
    path('comments/create/' , views.CreateCommentView.as_view())

]
