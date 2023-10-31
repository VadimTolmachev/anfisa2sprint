from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True,  verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(
        default=100, verbose_name='Порядок отображени'
    )

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Topping(PublishedModel):
    title = models.CharField(max_length=256,  verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256,  verbose_name='Название')

    class Meta:
        verbose_name = 'Обёртку'
        verbose_name_plural = 'Обёртки'


class IceCream(PublishedModel):
    title = models.CharField(max_length=256,  verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    is_on_main = models.BooleanField(default=False, verbose_name='На главную')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping)

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
