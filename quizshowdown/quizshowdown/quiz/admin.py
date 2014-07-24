from django.contrib import admin
from quizshowdown.quiz.models import Answer, Category, Question, UserProfile


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'accepted')
    inlines = [
        AnswerInline,
    ]

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfile)
