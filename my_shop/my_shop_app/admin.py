from django.contrib import admin
from .models import Category, Products, Order
from .forms import User_register

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(User_register)


