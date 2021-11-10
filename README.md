# interview-scheduler
This is a simple REST Web Api for online scheduling interviews. Implemented using Django-DRF.

## Features:
1. Interviewer/Interviewee can schedule an interview(POST).
2. HR can list all interviews by entering ids of interviewer and interviewee.
3. Token based authentication and role based authorization(HR, Interviewer, Interviewee, Admin)
4. Fully functional Django-Admin panel.

## UserStory:
User can register based on role and can login. Using that token interview can be scheduled. HR after logging in can view the schedules.

## Steps for Installation and Running:
1. Clone the repo using ```
git clone <reponame> ```
2.```cd <reponame>``` 
3. Grab a virtual environment and activate it
```
virtualenv <ur-env-name>
source <ur-env-name>/bin/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Update the DATABASE details in interview_schedule/settings.py with your credentials
  P.S: The right way to do it is using dotenv. And credentials are not to be exposed in production.
6. To run the project:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```
## Endpoints and response:
Use postman for executing API's(Swagger Integration is in the future scope)
API docs:
[API Docs](https://documenter.getpostman.com/view/11431269/UVC6hmYL)
Click here to watch some snapshots[Here](https://ibb.co/cg8RT99)

## Improvements and Future Scope:
1. Dockerization to be done
2. Scheduling is now based on date and assumption is an interviewer and interviewee can schedule interview once a day. It can be modified to different slots     within day.
