from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Staff)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(Report)


admin.site.site_header = "Childcare Management System Admin"
admin.site.site_title = "Childcare Management System Admin Portal"
admin.site.index_title = "Welcome to the Childcare Management System Admin Portal"