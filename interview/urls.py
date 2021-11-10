from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('schedule', views.create_interview_schedules),
    path('schedule/list', views.get_interview_schedules),
]

urlpatterns = format_suffix_patterns(urlpatterns)