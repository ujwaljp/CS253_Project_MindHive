from django.contrib import admin

from .models import Question
from answers.models import Answer
from comments.models import Comment

class AnswerInline(admin.TabularInline):
    model = Answer
    fk_name = 'to_question'
    extra = 0
    max_num = 3
    can_delete = False
    fields = ['text', 'author', 'pub_date']

class CommentInline(admin.TabularInline):
    model = Comment
    fk_name = 'parentObjQ'
    extra = 0
    max_num = 3
    can_delete = False
    fields = ['text', 'author', 'pub_date']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'show_description')
    list_filter = ('tags', 'pub_date', 'author')
    fields = ['title', 'text', ('author', 'pub_date'), 'anonymous', 'tags',
              'viewedBy', ('likedBy', 'dislikedBy')]
    inlines = [AnswerInline, CommentInline]