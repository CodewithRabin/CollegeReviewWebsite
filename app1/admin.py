from django.contrib import admin

from .models import College, Course, Review, Student

# Register your models here.
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Review)