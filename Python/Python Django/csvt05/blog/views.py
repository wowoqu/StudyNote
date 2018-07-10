from django.shortcuts import render,render_to_response

# Create your views here.
def index(req):
	title = 'Django csvt05'
	return render_to_response('index.html',locals())
