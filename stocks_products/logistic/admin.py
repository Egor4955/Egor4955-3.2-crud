from django.contrib import admin
from logistic.models import *

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(StockProduct)