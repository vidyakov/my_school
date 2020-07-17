from django.contrib import admin

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'name', 'author', 'price'
    list_display_links = list_display
