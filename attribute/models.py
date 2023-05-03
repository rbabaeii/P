from django.db import models
from product.models import Product
from utils.models import AbstracId, Images
from category.models import Category


class AttributeGroup(AbstracId):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='attribute_group')

    def __str__(self) -> str:
        return self.title

class Attribute(AbstracId):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    attribute_type = models.CharField(max_length=50, verbose_name='نوع')
    Attribute_group = models.ForeignKey(AttributeGroup, on_delete=models.CASCADE,verbose_name='attribute')

    def __str__(self) -> str:
        return self.title

class AttributeItem(AbstracId):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    Attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class ProductAttribute(AbstracId):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.Attribute.title + '\t : ' + self.value