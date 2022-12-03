from django.contrib import admin
from .models import OtherUser
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
# Register your models here.

class CustomAdmin(UserAdmin):
    add_form = CreatedUser
    form = ChangeUser
    model = OtherUser


admin.site.register(OtherUser,CustomAdmin)