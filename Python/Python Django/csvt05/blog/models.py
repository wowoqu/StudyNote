from django.db import models

sex_choices = (
	('f','female'),
	('m', 'male'),
)

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	sex = models.CharField(max_length=1,choices=sex_choices)
	phone = models.CharField(max_length=11)
	email = models.EmailField()
	addr = models.CharField(max_length=40)
	birth = models.DateField()
	pub_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name
