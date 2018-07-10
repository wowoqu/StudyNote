from django.contrib import admin
from blog.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('name','age','birth','phone','email')#列表显示
	list_per_page = 50                             #列表每页显示多少条信息
	list_display_links = ('name',)				   #列表可编辑字段
	# list_editable = ['name',]
	search_fields = ('name','age','birth',)		#可以查询的字段，增加查询框
	list_filter = ('name','age','birth',)					#查询的结果在进行过滤的过滤器，增加过滤框
	date_hierearchy = 'pub_date'						
	ordering = ('-pub_date',)				#列表按照这些字段依次进行排序，逆序在前面加-号
	

admin.site.register(User,UserAdmin)

		
