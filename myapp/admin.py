
# Register your models here.


from django.contrib import admin
from .models import User, Task

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'id')  

admin.site.register(User, UserAdmin)
admin.site.register(Task)
