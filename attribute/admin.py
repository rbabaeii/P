from django.contrib import admin
from .models import AttributeGroup, Attribute, AttributeItem, ProductAttribute

admin.site.register(AttributeGroup)
admin.site.register(Attribute)
admin.site.register(AttributeItem)
admin.site.register(ProductAttribute)
