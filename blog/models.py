from django.db import models
from authentication.models import User
from product.models import Product
from uuid import uuid4
from django.utils.text import  slugify
from datetime import datetime
from utils.api.utils import upload_image_path
from utils.models import AbstracId

class Blog(AbstracId):

    owner = models.ForeignKey(User , on_delete=models.CASCADE , related_name= 'blog')
    title = models.CharField(verbose_name= 'موضوع' , max_length = 200)
    body = models.TextField(verbose_name=  'توضیحات')
    image = models.ImageField(verbose_name='تصویر اگهی' , upload_to= upload_image_path , null= True , blank= True)
    slug = models.SlugField(verbose_name= 'عبارت لینک' , unique = True , null= True , blank= True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')
    publish_at = models.DateTimeField(verbose_name= 'زمان انتشار' , null= True , blank= True , )

    def save(self):
        if self.slug == None:
            value = self.title + '-' + uuid4().hex
            self.slug = slugify(value=value)
        super(Blog , self).save()

    def __str__(self) -> str:
        return self.title


class Comment(AbstracId):
    Blog = models.ForeignKey(Blog , on_delete= models.CASCADE , related_name='comments')
    user = models.ForeignKey(User , on_delete= models.CASCADE , related_name= 'comments')
    text = models.TextField(verbose_name='متن')
    parent = models.ForeignKey('self' , on_delete= models.SET_NULL , related_name= 'replies' , null= True , blank= True)
    published = models.BooleanField(default= False)

    def __str__(self) -> str:
        return self.text[:20]