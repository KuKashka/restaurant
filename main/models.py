from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва категорії')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']
    
class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва страви')
    available = models.BooleanField(default=True, verbose_name='Доступність страви')
    description = models.TextField(null=True, blank=True, verbose_name='Опис страви')
    ingredients = models.TextField(null=True, blank=True, verbose_name='Інгредієнти')
    image = models.ImageField(upload_to='dishes/', null=True, blank=True, verbose_name='Зображення страви')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Ціна страви')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name='Категорія страви')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
        ordering = ['name']
    

class Order(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Готівка'),
        ('card', 'Картка'),
        ('online', 'Онлайн-оплата'),
    ]
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Користувач', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Ім\'я замовника')
    phone = models.CharField(max_length=20, verbose_name='Телефон замовника')
    adress = models.CharField(max_length=255, verbose_name='Адреса доставки')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS, verbose_name='Спосіб оплати')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Загальна ціна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата замовлення')
    comments = models.TextField(null=True, blank=True, verbose_name='Коментарі до замовлення')

    def __str__(self):
        return f'Замовлення: {self.pk} x {self.created_at} - {self.total_price} грн'
    
    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
        ordering = ['-created_at']


class DishInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='dishes_in_order', verbose_name='Замовлення')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='orders_with_dish', verbose_name='Страва')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кількість')

    def __str__(self):
        return f'{self.dish.name} x {self.quantity}'

    class Meta:
        verbose_name = 'Страва в замовленні'
        verbose_name_plural = 'Страви в замовленнях'

    
class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Користувач')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews', verbose_name='Страва')
    rating = models.PositiveIntegerField(default=5, verbose_name='Рейтинг')
    comment = models.TextField(null=True, blank=True, verbose_name='Коментар до страви')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата відгуку')

    def __str__(self):
        return f'Відгук на {self.dish.name} - Рейтинг: {self.rating}'

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ['-created_at']

# Create your models here.
