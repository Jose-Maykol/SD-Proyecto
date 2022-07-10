from django.contrib import admin

from expenses.models import Category, Expenses

admin.site.register(Category)
admin.site.register(Expenses)
