from rest_framework import serializers
from attribute.models import AttributeGroup, Attribute, AttributeItem, ProductAttribute
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id' ,'title' , 'parent' , 'keyword' , 'description' , 'status' , 'Image')

class AttributeGroupSerializer(serializers.ModelSerializer):
    Category = CategorySerializer()
    class Meta:
        model = AttributeGroup
        fields = ('id','title' , 'Category')


class AttributeSerializer(serializers.ModelSerializer):
    Attribute_group = AttributeGroupSerializer()
    class Meta:
        model = Attribute
        fields = ('id' , 'title' ,'attribute_type' , 'Attribute_group')


class AttributeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeItem
        fields = ('id' , 'title' , 'Attribute')

class ProductAttributeSerializer(serializers.ModelSerializer):
    def get_product(self , obj):
        return obj.Product.title
    Product = serializers.SerializerMethodField(method_name='get_product')
    class Meta:
        model = ProductAttribute
        fields = '__all__'

class CreateProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = "__all__"

    def validate(self, attrs):
        product = attrs['Product']
        attribute = attrs['Attribute']
        if product.Category.id == attribute.Attribute_group.Category.id:
            return attrs
        else :
            return serializers.ValidationError('Attribute most be in Category !')