from django.contrib import admin
from .models import Employee
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    exclude=('date_created',)
    list_display = ('employee_name','designation','phone_number','address')

admin.site.register(Employee,MovieAdmin)