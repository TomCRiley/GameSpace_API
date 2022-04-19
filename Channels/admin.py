from django.contrib import admin
from .models import *

# Register your models here.


class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'createdDate')


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'release_date')


admin.site.register(Channel, ChannelsAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Platform)
admin.site.register(Developer)
