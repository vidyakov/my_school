from django.views.generic import DetailView, ListView

from .models import Course


class AllCoursesListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
