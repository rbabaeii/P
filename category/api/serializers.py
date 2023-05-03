from rest_framework import serializers
from category.models import Category, Brand
from attribute.api.serializers import AttributeGroup


class CategorySerializer(serializers.ModelSerializer):
    attribute_group = AttributeGroup()

    class Meta:
        model = Category
        fields = ['id', 'create_at', 'title', 'en_title', 'keyword', 'description', 'status', 'slug', 'creat_at',
                  'update_at', 'parent', 'Image', 'attribute_group']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
