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

