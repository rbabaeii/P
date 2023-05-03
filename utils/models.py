from django.db import models
from .api.utils import upload_image_path
from uuid import uuid4
from django.utils import timezone
from django.conf import settings
from storages.backends.ftp import FTPStorage
FTP_FILE_STORAGE = FTPStorage()

class AbstracId(models.Model):
    id = models.UUIDField(verbose_name='ایدی' , primary_key=True , editable= False , unique= True , default= uuid4) 
    create_at = models.DateTimeField(verbose_name='زمان ایجاد' ,default= timezone.now)
    
    class Meta:
        abstract = True


class Images(AbstracId):
    title = models.CharField(max_length=50, blank=False, verbose_name='عنوان')
    image = models.ImageField(blank=False, upload_to=upload_image_path,  storage=FTP_FILE_STORAGE , verbose_name='تصویر')
    alt = models.CharField(verbose_name='seo alt' , max_length=50 , null = True , blank= True)

    def __str__(self):
        return self.title
    


    def get_image(self):
        image_url = self.get_url(self.image.url) if self.image else None
        return image_url

    @classmethod
    def get_url(cls, path):
        return f"{settings.FTP_STORAGE_ADDRESS}/images{path.split('images')[-1]}"


    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
