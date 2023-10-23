from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator
from django.db import models


class Item(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', validators=[MinValueValidator(1)])
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    name = models.CharField(max_length=150, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')


class Tag(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', validators=[MinValueValidator(1)])
    name = models.CharField(max_length=150, verbose_name='Название')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг',
                            validators=[RegexValidator(r'^[a-zA-Z0-9-_]+$')])


class Category(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', validators=[MinValueValidator(1)])
    name = models.CharField(max_length=150, verbose_name='Название')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Слаг',
                            validators=[RegexValidator(r'^[a-zA-Z0-9-_]+$')])
    weight = models.IntegerField(default=100, verbose_name='Вес',
                                 validators=[MinValueValidator(0), MaxValueValidator(32767)])
