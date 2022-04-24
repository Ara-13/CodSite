from django.contrib import admin
from . import models

@admin.register(models.Group)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Product)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.EP)
class AccountAdmin(admin.ModelAdmin):
    pass