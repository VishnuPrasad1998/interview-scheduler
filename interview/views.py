from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework import status
import interview
from utils.decorators import allowed_users
from rest_framework.decorators import api_view
from .models import InterviewSchedule
from .serializers import InterviewScheduleSerializer, InterviewScheduleListSerializer
from datetime import datetime
from django.db.models import Q

@api_view(['POST'])
@allowed_users(allowed_roles=['Interviewer', 'Interviewee'])
def create_interview_schedules(request):
    scheduled_date = datetime.strptime(request.data['scheduled_date'], '%Y-%m-%d').date()
    interviews = InterviewSchedule.objects.filter(interviewer_id=request.data['interviewer'], \
        interviewee_id=request.data['interviewee'], scheduled_date=scheduled_date)
    if interviews:
        return Response({"data": "Sorry, Schedule already exist for {0} pick another day".format(scheduled_date)}, status=status.HTTP_201_CREATED)
    serializer = InterviewScheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"data": "Successfully Scheduled"}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@allowed_users(allowed_roles=['Hr'])
def get_interview_schedules(request):
    interviewer_id = request.GET.get('interviewer_id')
    interviewee_id = request.GET.get('interviewee_id')
    interviews = InterviewSchedule.objects.filter(interviewer_id=interviewer_id, interviewee_id=interviewee_id)
    serializer = InterviewScheduleListSerializer(interviews, many=True)
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)
