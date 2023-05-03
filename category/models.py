from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from utils.models import AbstracId, Images
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(AbstracId, MPTTModel):
    STATUS = (
        ('True', "فعال"),
        ("False", "غیرفعال")
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL,
                            verbose_name='دسته‌مادر')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    en_title = models.CharField(max_length=50, verbose_name='عنوان انگلیسی')
    keyword = models.CharField(max_length=250, verbose_name='کلمه کلیدی')
    description = models.CharField(max_length=300, verbose_name='توضیحات')
    status = models.CharField(max_length=50, choices=STATUS, verbose_name='وضعیت')
    Image = models.ForeignKey(Images, on_delete=models.CASCADE, verbose_name="تصویر", related_name="images")
    slug = models.SlugField(verbose_name='عبارت لینک', blank=True, null=False, unique=True, allow_unicode=True,
                            max_length=200)
    # creat_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاده شده در تاریخ')
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته‌بندی‌'

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('product_category_list', kwargs={'slug': self.slug})

    def category_active(self):
        return self.objects.filter(status=True)

    def save(self, *args, **kwargs):
        is_slug = bool(Category.objects.filter(slug=self.en_title))
        if self.slug == '':
            if is_slug:
                self.slug = slugify(self.en_title + str(self.id))
            else:
                self.slug = slugify(self.en_title)
        super().save(*args, **kwargs)


class Brand(AbstracId):
    name = models.CharField(max_length=50, verbose_name='نام برند')
    description = models.CharField(max_length=300, verbose_name='توضیحات')
    slug = models.SlugField(verbose_name='عبارت لینک', blank=True, null=False, unique=True, allow_unicode=True,
                            max_length=200)

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'دسته‌بندی برند'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_slug = bool(Category.objects.filter(slug=self.name))
        if self.slug == '':
            if is_slug:
                self.slug = slugify(self.name + str(self.id))
            else:
                self.slug = slugify(self.name)
        super().save(*args, **kwargs)
