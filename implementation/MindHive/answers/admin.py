from django.contrib import admin
from .models import Answer

# Register your models here.
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('show_description', 'author', 'pub_date', 'to_question')
    fieldsets = (
        (None, {
            'fields': ('text', 'to_question', ('author', 'pub_date'), 'anonymous')
        }),
        ('Votes', {
            'fields': (('likedBy', 'dislikedBy'),)
        })
    )
    