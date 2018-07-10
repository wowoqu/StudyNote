from django.shortcuts import render,render_to_response
from blog.models import Employee,Entry,Blog

# Create your views here.
def index(req):
	db = {'title':'Django 数据库'}
	emps = Employee.objects.all()
	many_to_one = Entry.objects.all()
	return render_to_response('index.html',locals())
