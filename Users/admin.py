from django.contrib import admin
from Users.models import CustomUser
from .models import CustomUser
# Register your models here.

admin.site.register(CustomUser)
