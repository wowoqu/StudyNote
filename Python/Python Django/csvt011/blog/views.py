from django.shortcuts import render,render_to_response


class Person1():
	"""docstring for Person"""
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
		


# Create your views here.
def index(req):
	user = {'name':'laowang','age':23,'sex':'male'}
	person = Person1('tom',23,'male')
	return render_to_response('index1.html',{'title':'abc','user':user,'person':person})
