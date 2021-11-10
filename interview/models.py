from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Interviewer(models.Model):
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    details = models.TextField(blank=True)
    def __str__(self):
        return self.interviewer.first_name +" "+self.interviewer.last_name

class Interviewee(models.Model):
    interviewee = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    details = models.TextField(blank=True)
    def __str__(self):
        return self.interviewee.first_name+" "+self.interviewee.last_name

class InterviewSchedule(models.Model):
    interviewer = models.ForeignKey(Interviewer, on_delete=models.DO_NOTHING)
    interviewee = models.ForeignKey(Interviewee, on_delete=models.DO_NOTHING)
    scheduled_start_time = models.TimeField()
    scheduled_end_time = models.TimeField()
    scheduled_date = models.DateField()
    posting_date = models.DateTimeField(default=datetime.now, blank=True)
    meeting_link = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.interviewer.interviewer.first_name + "->" +  self.interviewee.interviewee.first_name