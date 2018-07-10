from django.db import models
import pymysql

# Create your models here.
class Employee(models.Model):
	"""docstring for Employee"""
	# def __init__(self, arg):
	# 	super(Employee, self).__init__()
	# 	self.arg = arg
	name = models.CharField(max_length=20)
	age = models.CharField(max_length=10)
	# addr = models.CharField(max_length=60)

	# def __unicode__(self):
	# 	return self.name

	def __str__(self):
		return self.name

class Entry(models.Model):

	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Blog(models.Model):

	name = models.CharField(max_length=20)
	entry = models.ForeignKey(Entry,on_delete=models.CASCADE)

	def __str__(self):
		return self.name
