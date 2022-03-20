from django.contrib import admin
from .models import Comment


# Register the Comment model with the admin site and customise its admin view
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('show_description', 'author', 'pub_date', 'parentObjType')
    fieldsets = (
        (None, {
            'fields': ('text', ('author', 'pub_date'))
        }),
        ('Parent Object', {
            'fields': ('parentObjType', ('parentObjQ', 'parentObjA'))
        }),
        ('Votes', {
            'fields': (('likedBy', 'dislikedBy'),)
        })
    )
