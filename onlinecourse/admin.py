from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here

class ChoiceInline(admin.StackedInline):
    model = Choice


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]


class LessonInline(admin.StackedInline):
    model = Lesson
    inlines = [Question]
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
@@ -19,12 +29,12 @@ class CourseAdmin(admin.ModelAdmin):


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

    inlines = [QuestionInline, ]

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
