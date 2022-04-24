from django.contrib import admin
from . import models

@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.CodAccount)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Image)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Video)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Link)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Order)
class CodOrderAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Cart)
class CodCartAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Slider)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ResponsiveSlider)
class CodOrderAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Banner)
class CodCartAdmin(admin.ModelAdmin):
    pass