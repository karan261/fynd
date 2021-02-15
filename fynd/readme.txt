This django project is used for creating restfull api for Movie

Creating a django project: django-admin startproject projectname

Creating a django app: python manage.py startapp appname

manage.py: A command-line utility that lets you interact with this Django project in various ways.

Running a Server: python manage.py runserver


Public IPv4 address:52.89.167.14

Scalabilty Problem:This problem can be resolved easily by deploy our app in aws,firstly we create a ec2 instance after successfully launching the ec2 instance their is option of autoscaling in ec2 now to use this feature of ec2 we have to first configure its autoscaling group setting by provide instance information(how many instance required to run a particular application) then provide thresold value of given instance on basis of (average cpu utilisation,application load balancer etc) after successfully confiqure auto scaling group our app  is ready for auto scale up and scale down and this scale up to scale down and vice versa itself takes care by Amazon.
