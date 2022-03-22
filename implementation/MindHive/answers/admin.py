from django.contrib import admin
from .models import Answer
from comments.models import Comment


# ContentInlineForAns class provides a list of comments under an answer in the admin view
class CommentInlineForAns(admin.TabularInline):
    model = Comment
    fk_name = 'parentObjA'
    extra = 0
    max_num = 3
    can_delete = False
    fields = ['text', 'author', 'pub_date']


# Register the Answer model with the admin site and customise its admin view
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
    inlines = [CommentInlineForAns]
