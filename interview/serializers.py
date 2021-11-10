from django.contrib.auth.models import User
import interview
from .models import InterviewSchedule, Interviewer
from rest_framework import serializers

        
class InterviewScheduleListSerializer(serializers.ModelSerializer):
    interviewer = serializers.CharField(source='interviewer.interviewer.first_name')
    interviewee = serializers.CharField(source='interviewee.interviewee.first_name')
    class Meta:
        model = InterviewSchedule
        fields = ['scheduled_start_time', 'scheduled_end_time', 'scheduled_date', 'posting_date', 'meeting_link', 
                'interviewee', 'interviewer']
        
class InterviewScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSchedule
        fields = '__all__'
