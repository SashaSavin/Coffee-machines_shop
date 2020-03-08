from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # хэширование паролей
from django.forms import forms

from orders.models import User, Product, Order, Comment
from django import forms


User_client = User.objects.filter(user_type = 'CL')
User_manager = User.objects.filter(user_type = 'MN')


admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment)

