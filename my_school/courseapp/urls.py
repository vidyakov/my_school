from django.urls import re_path

from courseapp.views import CourseDetailView


app_name = 'courseapp'

urlpatterns = [
    re_path(r'(?P<pk>\d+)/$', CourseDetailView.as_view(), name='page')
]
