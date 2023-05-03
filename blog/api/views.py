from django.shortcuts import render
from blog.models import Blog, Comment
from rest_framework.views import APIView, Response, status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import (ListBlogSerializer,
                          RetriveUpdateDestroyBlogSerializer, ListCommentSerializer,
                          CreateCommentSerializer)


class ListActiveBlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = ListBlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RetriveUpdateDestroyBlogView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Blog.objects.all()
    serializer_class = RetriveUpdateDestroyBlogSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated,)


class ListCommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        queryset = Comment.objects.filter(Blog__id=pk)
        serializer = ListCommentSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    permission_classes = (IsAuthenticated ,)
    def get(self , request , pk):
        queryset = Comment.objects.filter(Blog__id = pk)
        serializer = ListCommentSerializer(queryset , many = True)
        return Response(data = serializer.data , status= status.HTTP_200_OK)

class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes = (IsAuthenticated ,)
