from django.contrib import admin

from .models import User, Report

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'blocked', 'date_joined')
    exclude = ('groups', 'user_permissions', 'first_name', 'last_name')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_text', 'reporter', 'reportedUser', 'reportedObjType')
    list_filter = ('reportedUser',)