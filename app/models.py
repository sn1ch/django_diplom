from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='Наименование')
    specification = models.TextField(verbose_name='Описание')
    slug_name = models.SlugField()
    img = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Изображение')
    departament = models.ForeignKey('Departament', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Departament(models.Model):
    name = models.CharField(max_length=250)
    slug_name = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Topic(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    product = models.ManyToManyField('Product', through='TopicProduct')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья на главную страницу'
        verbose_name_plural = 'Статьи на главную страницу'


class TopicProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Статья на главную страницу'
        verbose_name_plural = 'Статьи на главную страницу'


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class Order(models.Model):
#     user = models.ManyToManyField('User')
#     products = models.ManyToManyField(Product)
