from django.contrib import admin
from .models import employee,Department,Role
# Register your models here.

admin.site.register(employee)
admin.site.register(Department)
admin.site.register(Role)