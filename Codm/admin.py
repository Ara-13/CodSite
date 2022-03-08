from django.contrib import admin
from . import models

@admin.register(models.CodAccount)
class CodAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Video)
class CodAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Link)
class CodAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Order)
class CodOrderAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Cart)
class CodCartAdmin(admin.ModelAdmin):
    pass

