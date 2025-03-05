# from datetime import datetime
# from tkinter import image_types
# from xmlrpc.client import Boolean

from django.db import models
from django.forms import Field


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name='Модель телефона')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(default=None, verbose_name='Изображение') #upload_to='https://avatars.mds.yandex.net/get-mpic/'
    release_date = models.DateField(default=None, verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(default=None, verbose_name='LTE')
    slug = models.SlugField(blank=True, unique=True)