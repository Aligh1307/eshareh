from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس عنوان')
    picture = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='تصویر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children',
                               verbose_name='والد')

    def __str__(self):
        return self.title


class Word(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس عنوان')
    pronunciation = models.CharField(max_length=100, null=True, blank=True, verbose_name='تلفظ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='words', verbose_name='دسته بندی')
    picture = models.ImageField(upload_to='media', verbose_name='عکس')
    video = models.FileField(upload_to='media', verbose_name='ویدیو')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')
    favorite = models.ManyToManyField(User, related_name='favorite_words', verbose_name='علاقه مندی ها')

    def __str__(self):
        return self.title
