from django.db import models
from django.contrib.auth.models import AbstractUser


PAID = 'ОПЛАЧЕНО'
UNPAID = 'НЕОПЛАЧЕНО'
DELIVERY = 'В ДОСТАВКЕ'

STATUS_CHOICES = (
    (PAID, 'ОПЛАЧЕНО'),
    (UNPAID, 'НЕОПЛАЧЕНО'),
    (DELIVERY, 'В ДОСТАВКЕ'),

)


class User(AbstractUser):
    user_type = models.CharField(max_length=2, default='test', choices=[
        ('MN', 'Manager'), ('CL', 'Client')], verbose_name='Пользователи')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Product(models.Model):
    image = models.CharField(max_length=100, verbose_name='Изображение товара')
    description = models.TextField(
        blank=True, null=True, default=None, verbose_name='Описание товара')
    name = models.CharField(max_length=100, verbose_name='Наименование товара')
    price = models.CharField(max_length=100, verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '{}'.format(self.name)


class Order(models.Model):
    products_list = models.ManyToManyField(Product, verbose_name='Список товаров')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_orders', verbose_name='Менеджер')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_orders', verbose_name='Клиент')
    author = models.CharField(max_length=100, verbose_name='Автор')
    number = models.IntegerField(verbose_name='Номер')
    order_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name='Сумма заказа')
    date_and_time_of_order = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name='Создан')
    date_and_time_of_change_of_order = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name='Обновлён')
    order_status = models.CharField(
        max_length=50, default=UNPAID, choices=STATUS_CHOICES, verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Comment(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, primary_key=True)

    author = models.OneToOneField(
        User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True,
                            default=None, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
