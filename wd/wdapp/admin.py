from django.contrib import admin

# Register your models here.
from wdapp.models import Company, Business, Driver, Cargo, OrderStatus, BusinessOrder, DriverExpense, Stop,CargoManifest, Trip
admin.site.register(BusinessOrder)
admin.site.register(Driver)
admin.site.register(OrderStatus)
admin.site.register(CargoManifest)
admin.site.register(Business)
admin.site.register(Stop)
admin.site.register(Trip)
admin.site.register(Cargo)
admin.site.register(DriverExpense)
