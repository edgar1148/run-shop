from django.contrib.auth import get_user_model
from django.db import models

from shop.models import Product

User = get_user_model()


class ShippingAddress(models.Model):
    """Модель адреса доставки"""
    full_name = models.CharField(
        max_length=100,
        verbose_name='Полное имя'
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Электронная почта'
    )
    street_address = models.CharField(
        max_length=100,
        verbose_name='Улица'
    )
    apartment_address = models.CharField(
        max_length=100,
        verbose_name='Номер квартиры'
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Страна'
    )
    zip_code = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Индекс'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Пользователь'
    )

    # address_type = models.CharField(max_length=1, choices=(('B', 'Billing'), ('S', 'Shipping')))
    # default = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'

    def __str__(self):
        return "Shipping Address" + str(self.id)


class Order(models.Model):
    """Модель заказа"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Пользователь'
    )
    shipping_address = models.ForeignKey(
        ShippingAddress,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Адрес доставки'
    )
    amount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Сумма',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлен'
    )
    paid = models.BooleanField(
        default=False,
        verbose_name='Оплачен'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return "Заказ - " + str(self.id)


class OrderItem(models.Model):
    """Модель элемента заказа"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Продукт'
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Цена',
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name='Количество',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return "OrderItem" + str(self.id)
