from django.db import models
from utils.models import AbstracId, Images


class Configure(AbstracId, models.Model):
    web_title = models.CharField(max_length=255, verbose_name='موضوع سایت')
    nav_icon = models.ForeignKey(Images, null=True, blank=True, on_delete=models.CASCADE, related_name='van_icon',
                                 verbose_name='ناو آیکون')
    site_description = models.CharField(max_length=255, verbose_name='توضیحات سایت')
    fav_icon = models.ForeignKey(Images, null=True, blank=True, on_delete=models.CASCADE, related_name='fac_icon',
                                 verbose_name='فاو آیکون')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.web_title
