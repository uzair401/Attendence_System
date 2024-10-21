from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
#Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(staff)
admin.site.register(Subject)
admin.site.register(Staff_leave)
admin.site.register(Student_leave)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)
