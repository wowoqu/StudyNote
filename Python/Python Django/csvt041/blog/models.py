from django.db import models

sex_choices = (
		('f','famale'),
		('m','male'),
)

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=30)
	age = models.CharField(max_length=20)
	# sex = models.CharField(max_length=1,choices=sex_choices)
	addr = models.CharField(max_length=60)
	# birth = models.DateField(blank=True,null=True)
	phone = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	# pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
