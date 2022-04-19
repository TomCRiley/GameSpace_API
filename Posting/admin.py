from django.contrib import admin
from .models import *
# Register your models here.


# class MainPostAdmin(admin.ModelAdmin):
#     list_display = ('username', 'createdDate')


admin.site.register(MainPost)
