from django.shortcuts import render,render_to_response
from django.template import loader,Template
from django.http import HttpResponse

# Create your views here.
def index(req):
	title = {'user':'root','passwd':123456}
	return render_to_response('index1.html',{'title':title})

def index1(req):
	t = loader.get_template('index1.html')
	title = {'user':'root','passwd':123456}
	html = t.render(title)
	return HttpResponse(html)

def index2(req):
	t = Template('<h1>hello</h1>','')
	c = {'title':'abc'}
	# return HttpResponse(t.render())
	return render_to_response(t.template,{})

def index3(req):
	title = {'user':'root','passwd':123}
	d_list = [1,2,3,4,5]
	return render_to_response('index2.html',locals())
