from django.contrib import admin
from blog.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('name','age','sex','phone','addr','birth','pub_date','email')
	list_filter = ('pub_date','birth')					#查询的结果在进行过滤的过滤器，增加过滤框
	date_hierearchy = 'birth'						
	ordering = ('-pub_date',)				#列表按照这些字段依次进行排序，逆序在前面加-号
	search_fields = ('birth','name')




admin.site.register(User,UserAdmin)
		
