# interview-scheduler
This is a simple REST Web Api for online scheduling interviews. Implemented using Django-DRF.

## Features:
1. Interviewer/Interviewee can schedule an interview(POST).
2. HR can list all interviews by entering ids of interviewer and interviewee(GET).
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
7. After creating users via API/Admin dashboard and super user Admin should enter the admin portal and should add users to their corresponding interviewer/interviewee model. This is done based on an assumption. Can be made better by adding this step at the registration flow itself.

## Endpoints and response:
Use postman for executing API's(Swagger Integration is in the future scope)
API docs:
[API Docs](https://documenter.getpostman.com/view/11431269/UVC6hmYL)
Click here to watch some snapshots[Here](https://ibb.co/cg8RT99)

## Assumptions:
1. A interviewer-Interviewee can schedule one interview a day
2. Time format in which is scheduled is From-HH:MM:SS To-HH:MM:SS(It can be updated to multiple choices like 10am-11am etc)
3. Superuser/Admin adds users into particular type(Interviewer/Interviewee Foreign key relationship establishment with users) should changed into such a way that it is to be done automatically in registration time.

## Improvements and Future Scope:
1. Dockerization to be done
2. Scheduling is now based on date and assumption is an interviewer and interviewee can schedule interview once a day. It can be modified to different slots     within day.
3. Remove secretkey/dbcredentials inorder to avoid vulnerabilities.
4. Mapings can be implemented between interview slots.

