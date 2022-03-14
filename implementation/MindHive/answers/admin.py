from django.contrib import admin
from .models import Answer
# Register your models here.
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'pub_date', 'parentObj')
    fieldsets = (
        (None, {
            'fields': ('text', 'ques', ('author', 'pub_date'), 'anonymous')
        }),
        ('Votes', {
            'fields': (('likedBy', 'dislikedBy'),)
        })
    )