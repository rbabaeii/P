from rest_framework import generics
from attribute.models import AttributeGroup, Attribute, AttributeItem, ProductAttribute
from .serializers import AttributeGroupSerializer, AttributeSerializer, AttributeItemSerializer, \
    ProductAttributeSerializer , CreateProductAttributeSerializer
from rest_framework.views import APIView , Response , status
from product.models import Product

class AttributeGroupView(APIView):
    def get(self , request , pk):
        queryset = AttributeGroup.objects.filter(Category__id = pk)
        serializer = AttributeGroupSerializer(queryset , many = True)
        return Response(data = serializer.data , status= status.HTTP_200_OK)

class AttributeView(APIView):
    def get(self , request , pk):
        queryset = Attribute.objects.filter(Attribute_group__Category__id = pk)
        serializer = AttributeSerializer(queryset , many = True)
        return Response(data = serializer.data , status= status.HTTP_200_OK)

class AttributeItemView(generics.ListAPIView):
    def get(self , request , pk):
        queryset = AttributeItem.objects.filter(Attribute__Attribute_group__Category__id = pk)
        serializer = AttributeItemSerializer(queryset , many = True)
        return Response(data = serializer.data , status= status.HTTP_200_OK)


class ProductAttributeView(APIView):
    def get(self , request , pk):
        queryset = ProductAttribute.objects.filter(Product__id = pk)
        serializer = ProductAttributeSerializer(queryset , many = True)
        return Response(data = serializer.data , status= status.HTTP_200_OK)


class CreateProductAttributeView(generics.CreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = CreateProductAttributeSerializer
    def post(self, request):
        data = request.data
        if isinstance(data , list):
            serializer = self.get_serializer(data = data , many = True)
        else :
            serializer = self.get_serializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data , status = status.HTTP_200_OK)
        else :
            return Response()