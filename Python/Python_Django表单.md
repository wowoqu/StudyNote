## Python Django Form(表单)
+ 创建项目 django-admin.exe startproject CSVT
+ 创建APP django-admin.exe startapp blog
+ settings.py
    * > 添加blog,INSTALLED_APPS = [
            ...
            'blog',]
    * > 去除csrf模块，MIDDLEWARE = [
    ...
    \# 'django.middleware.csrf.CsrfViewMiddleware',
    ...]
    或者在index.html模块中的form中添加{% csrf_token %}
+ urls.py
    * from blog.views import *
    * url(r'^blog/register',register)
+ views.py

        from django.http import HttpResponse
        from django.shortcuts import render,render_to_response
        from django import forms

        class Userform(forms.Form):
            name = forms.CharField() #相当于 name:<input type="text" name="">
            age = forms.CharField()  #相当于 age:<input type="text" name="">
            addr = forms.CharField() #相当于 addr:<input type="text" name="">
        #创建form对象,form表单的提交模块


        # Create your views here.
        def register(req):
            title = 'Django 表单 初步'
            if req.method == 'POST':              
                #判断表单是否是post提交，不是则执行else
                form = Userform(req.POST)         #获取当前post提交的form对象
                if form.is_valid():               #判断form值是否正确
                    # print(form.cleaned_data)      #输出表单字典在服务器上
                    # return HttpResponse('OK!')    #index.html上渲染ok！
                    rdict = form.cleaned_data
                    return render_to_response('index.html',locals())  #渲染到index上
            else:
                form = Userform()     #初始化form表单
            return render_to_response('index.html',locals())

                
HTML中遍历

        {% if rdict %}
        {% for k,v in rdict.items %}
            {{ k }} : {{ v }}
        {% endfor %}
        {% endif %}
            

## Django 获取html的post请求
HTML
        
        <form action="test" method="post">     #提交到test页面，方式为post
            <label for="user">User:</label>    #自己创建的form表单
            <input id="user" type="text" name="user">&nbsp;
            <label for="passwd">Passwd:</label>
            <input type="password" name="passwd">
            <input type="submit" value="提交">
        </form>
views.py

        def register(req):              #定义url调用的函数
            title = 'Django 表单 初步'
            if req.method == 'POST':      #判断是否是post提交
                # form = Userform(req.POST)         #获取当前post提交的form对象
                # if form.is_valid():               #判断form值是否正确
                #     print(form.cleaned_data)      #输出表单字典在服务器上
                #     return HttpResponse('OK!')    #index.html上渲染ok！
                    # rdict = form.cleaned_data
                    # return render_to_response('index.html',locals())
                user = req.POST.get('user')     #获取html的form中name='user'的值，这种取不到passwd类型的值
                也可以为user = req.POST['user']，这种可以
                passwd = req.POST.get('pass')
                print('user:'+ str(user))
                print('passwd' + str(passwd))
                print(req.POST)          #在服务器端打印
                return render_to_response('index.html',locals()) 将user,passwd变量传回去
            else:
                form = Userform()    #刚开始为get提交，执行这一段，初始化form类对象
            return render_to_response('index.html',locals())
HTML中回显

        {% if user and passwd %}
            user: {{user}}<br>
            passwd:{{passwd}}
        {% endif %}

### req.POST 为request.QueryDict 对象 
可以在shell中导入 blog.views，然后request.QueryDict.,按tab键查询相应方法。

## Django 文件上传
### 第一种，在前端输入，并用open()  write() 方法保存
### index.html
    <div>用户注册</div>
    
    <form action="" method="post" enctype="multipart/form-data">
        {{ uf.as_p }}
        <!--  uf.as_p为将uf遍历显示出来 第一步 添加 enctype='multipart/form-data' -->
        <input type="submit" value="submit">
    </form>
### views.py
    from django.http import HttpResponse
    from django.shortcuts import render,render_to_response
    from django import forms
    from blog.models import User
    class Userform(forms.Form):
        username = forms.CharField()
        headImg = forms.FileField()  #创建文件上传对象，即html中的<input type="file">
    
    # Create your views here.
    def register(req):
        title = 'Django 文件上传'
        if req.method == 'POST':
            uf = Userform(req.POST,req.FILES) #第二步，添加req.FILES
            if uf.is_valid():
                # print(uf.cleaned_data['username']) #上面创建的类的属性
                # print(uf.cleaned_data['headImg']) #获取文件对象
                # print(uf.cleaned_data['headImg'].name) #获取文件对象名称
                # print(uf.cleaned_data['headImg'].size) #获取文件对象大小
                # fp = open('./templates/'+ uf.cleaned_data['headImg'].name,'wb')  
                #创建一个文件对象
                # s = uf.cleaned_data['headImg'].read()
                # #获取文件内容 ，用cleaned_date['headImg']文件对象的read方法
                # fp.write(s)  #写入内容
                # fp.close()
    
                #第二种 ，用数据库的方法
                user = User()
                user.username = uf.cleaned_data['username']
                user.headImg = uf.cleaned_data['headImg']
                user.save()
                print('name:' + str(user.username) + 'headImg:' + str(user.headImg) )
                return HttpResponse('OK')
        else:
            uf = Userform()
        return render_to_response('index.html',locals())    
### models.py
    from django.db import models
    
    # Create your models here.
    class User(models.Model):
        username = models.CharField(max_length=30)
        headImg = models.FileField(upload_to='./upload/')#必选参数,上传的位置，现在是当前目录下的upload文件夹
    
        def __str__(self):
            return self.username
### 第三种是创建后台，在后台的表中更改，上传数据。

### admin.py
    from django.contrib import admin
    from blog.models import User
    # Register your models here.
    class UserAdmin(admin.ModelAdmin):
        list_display = ('username','headImg',)
    
    admin.site.register(User,UserAdmin)

## Django Ajax
+ settings.py中，导入应用'blog',注释掉MIDDLEWARE = [] 中的csrf模块

### views.py
    from django.http import HttpResponse
    from django.shortcuts import render,render_to_response
    # from django.template import RequestContext
    # Create your views here.
    
    def tajax(req):
        if req.is_ajax():   #判断是否是ajax提交
            print('ajax')   
            if req.method == 'POST':  #判断是否是post提交
                print('post')
                print(req.body)      #获取ajax提交的元数据，
                print(req.POST)      #获取ajax修改后的数据
                
                # print(req.POST.get('date'))
                return HttpResponse(req.body) #返回给ajax的数据，success中的response
        else:
            return render_to_response('index.html',{}) #初始化页面用
### urls.py
    from django.conf.urls import url
    from blog.views import *
    
    urlpatterns = [
        # path('admin/', admin.site.urls),
        url(r'^index/$',tajax),
        url(r'^index/test/$',tajax), ajax 中的url地址，必须在这里有路由，即这里必须有该地址。
### 最后 index.html配置
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
         <script type="text/javascript" src="http://libs.baidu.com/jquery/1.11.1/jquery.min.js"></script>
    </head>
    <body>
    测试
    <form method="post">
    {#    {% csrf_token %}#}
        <input class="btna" type="button" value="提交">
    </form>
    </body>
    <script type="text/javascript" >
        $(function () {
            var data_list = [
                {'name':'chenchao','age':18},
                {'name':'lisi','age':19},
                {'name':'wangwu','age':13}
            ];  
            #要提交的数据，javascript中的json格式
            var test = JSON.stringify(data_list); #将javascript对象转为jsong格式
    
            console.log('初始化');
            $('.btna').click(function () {
                console.log('点击');
                $.ajax({
                    url : '/index/test/', #需要以斜杠结尾
                    type : 'POST',
                    data: test,
                    dateType : 'json',
                    success : function (response,status,xhr) {
                        console.log(response); 获取HttpResponse()中的内容
                        即为response
                    }
                });
            });
        })
    </script>
    </html>
