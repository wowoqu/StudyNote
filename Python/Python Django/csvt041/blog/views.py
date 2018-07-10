from django.shortcuts import render,render_to_response
from blog.models import User


# Create your views here.
def index(req):
	title = 'Django MySql'
	emp = User.objects.all()
	return render_to_response('index.html',locals())
