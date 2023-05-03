from django.contrib import admin
from .models import Images



# Image model

class ImageAdmin(admin.ModelAdmin):
    fields = ('title' , 'image' , 'alt')
    
admin.site.register(Images , ImageAdmin)