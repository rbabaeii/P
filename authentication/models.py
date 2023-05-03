from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.custom_usermanager import UserManager
from django.utils.html import format_html


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=256, unique=True)
    email = models.EmailField(max_length=256, null=True, blank=True, unique=True)
    national_code = models.CharField(max_length=256, null=True, blank=True)
    landline_phone = models.CharField(max_length=256, null=True, blank=True)
    father_name = models.CharField(max_length=256, null=True, blank=True)
    birth_date = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    post_code = models.CharField(max_length=256, null=True, blank=True)
    national_card_file = models.FileField(upload_to='user/files', null=True, blank=True)
    birth_certificate_file = models.FileField(upload_to='user/files', null=True, blank=True)
    wallet_inventory = models.PositiveIntegerField(default=0)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    otp_confirmed = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='user/photo', default='user/photo/default.png')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def __str__(self):
        return str(self.phone)

    def img(self):
        return format_html("<img style='width:30px;border-radius:50%;' src='{}'>".format(self.photo.url))

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
