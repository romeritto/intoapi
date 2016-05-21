from django.contrib import admin
from .models import Event, EventProduct, Guest, Product

# Register your models here.

admin.site.register(Event)
admin.site.register(EventProduct)
admin.site.register(Guest)
admin.site.register(Product)