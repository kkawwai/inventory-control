from django.contrib import admin
from .models import Product, Branch_one, Branch_two, Branch_three, Central_product
# Register your models here.

admin.site.register(Product),
admin.site.register(Branch_one),
admin.site.register(Branch_two),
admin.site.register(Branch_three),
admin.site.register(Central_product),
