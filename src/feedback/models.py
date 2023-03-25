from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    class Categories(models.TextChoices):
        ELECTRONICS = 'electronics', _('Электроника')
        FRUITS = 'fruits', _('Фрукты')
        MEATS = 'meats', _('Мясо')
        BOOKS = 'books', _('Книги')

    name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Название'
    )

    category = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        choices=Categories.choices,
        verbose_name='Категория'
    )

    description = models.TextField(
        max_length=4096,
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='product_img',
        verbose_name='Картинка продукта'
    )

    def __str__(self):
        return f'{self.name} {self.category}'


class Review(models.Model):
    class Rating(models.IntegerChoices):
        TERRIBLE = 1, _('Ужасно')
        BAD = 2, _('Плохо')
        NORMAL = 3, _('Нормально')
        GOOD = 4, _('Хорошо')
        GREAT = 5, _('Отлично')

    author = models.ForeignKey(
        User,
        related_name='author_review',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    product = models.ForeignKey(
        Product,
        related_name='product_review',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )

    review = models.CharField(
        max_length=1024,
        null=False,
        blank=False,
        verbose_name='Текст отзыва'
    )

    rating = models.IntegerField(
        null=False,
        blank=False,
        choices=Rating.choices,
        verbose_name='Оценка'
    )

    def __str__(self):
        return f'{self.author} {self.product} {self.rating}'
