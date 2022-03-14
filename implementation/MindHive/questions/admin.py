from django.contrib import admin

from .models import Question

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'text')
    list_filter = ('tags', 'pub_date', 'author')
    fields = ['title', 'text', ('author', 'pub_date'), 'anonymous', 'tags',
              'viewedBy', ('likedBy', 'dislikedBy')]