from django.db import models

# Create your models here.

sex_choices = (
		('f','famale'),
		('m','male'),
)

class User(models.Model):
	"""docstring for User"""

	name = models.CharField(max_length=30)
	sex = models.CharField(max_length=1,choices=sex_choices)
	city = models.CharField(max_length=60)
	# pub_data = models.DateField(blank=True,null=True)
	pub_date = models.DateTimeField(auto_now_add = True,blank=True,null=True)

	def __str__(self):
		# return ('%s-%s'%(self.name,self.sex))
		return self.name
	

		
