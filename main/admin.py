from django.contrib import admin
from .models import Category, Dish, Order, DishInOrder, Review

class DishInOrderInline(admin.TabularInline):
    model = DishInOrder
    extra = 3

# Register your models here.
admin.site.register(Category)
admin.site.register(Dish) 
admin.site.register(Order, inlines=[DishInOrderInline])
admin.site.register(DishInOrder)
admin.site.register(Review)