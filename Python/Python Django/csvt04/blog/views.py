from django.shortcuts import render,render_to_response
from blog.models import User

# Create your views here.
def index(req):
	title = 'Django 后台 MySQL'
	users = User.objects.all().values()
	return render_to_response('index.html',locals())


