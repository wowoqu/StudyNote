# Django Note
## 环境配置
>Windows下的环境配置
    打开powershell，先安装pip。
    安装完成之后输入：pip install Django
## 测试是否安装完成：
    >>> python
    >>> import django
    >>> django.VERSION

出现版本信息则说明安装完成

## 创建第一个项目
### 进入powershell，进入项目创建的位置。
>cd python
### 创建一个项目
>django-admin.exe startproject testdjango
### 进入项目文件夹中
>cd testdjango
### 更改setting.py文件夹。
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', #这是自己定义的应用，创建应用后要先在这里添加一下
    ]
### 更改urls.py文件。
    from django.conf.urls import url #导入url
    from blog.views import index     #从自己创建的应用的view中导入处理函数index

    urlpatterns = [
        # path('admin/', admin.site.urls),
        url(r'^index/$',index),     #前面是正则表达式，后面是对应的处理函数
                                    #当浏览器访问127.0.0.1:8000/index/ 时就会调用index函数
    ]    
### 创建第一个应用
>django-admin.exe startapp blog #这个就是刚才提到的应用blog
### 创建模板
    在blog文件夹下创建一个名为templates的文件夹，并在该文件夹下创建一个index1.html文件

index1.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试 Python Django V2.0</title>
</head>
<body>
<h1>这是第二次练习</h1>    
<span></span>
</body>
</html>

```

### 更改blog文件夹下面的views.py文件

#### 创建index函数
>from django.shortcuts import render,render_to_response
>
>def index(req):
>    return render_to_response('index1.html',{})



## Django模板变量
Django模板变量是由两个花括号组成的 ```{{}} ```,括号当中存贮模板变量
><title>{{user}}</title> #user为模板变量

+ 方法一
    * 在views.py 中通过render_to_response()方法的第二个参数传递，例如：    
```

def index(req):
    return            render_to_response('index1.html',{'user':'laowang','title':'abc'})
    
    \#通过传递一个字典变量来传递

```
+ 方法二
```
def index(req):
    user = {'name':'liming','age':23,'sex':'male'}
    return render_to_response('index1.html',user)  html: <li>{{name}}</li>

    或者 render_to_response('index1.html',{'user':user} html: <li> {{user.name}} </li>
```

+ 方法三
    * 创建一个类
```
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

```

### 调用
```
<span> {{title}} </span><br>
<span> {{user.name}} </span>
<span> {{person.name}} </span>
```

+ 方法四 创建一个list
booklist = ['java','php','html','python']
return render_to_response('index1.html',{'booklist':booklist})
调用 {{booklist.0}}

## Django执行顺序
+ django install
+ django-admin.exe startproject
+ django-admin.exe startapp
+ vim settings.py
    * app add --->blog
+ vim urls.py
    * url(r'^index/$',index)
+ vim blog/views.py
    * def index():
+ python manager.py runserver
    * url 127.0.0.1:8000/index

## Django模板标签
+ if标签
    * {% if 判断语句%}  //判断语句不可以包含括号，and和or不可以一起使用
    * {% else %}
    * {% endif %}       
+ for标签
    * {% for 语句 %}   //{% for k,v in dict.items %} //这里的方法不要加括号
    * {% endfor %}
    * 实例一

    ```
    {% for k,v in title.items %}
        <p>k: {{k}} &nbsp; v: {{v}} </p>
    {% endfor %}
    ```
+ 模板标签的值   
    * {{forloop.counter}} 相当于加一个序号 跟有序列表前面的序号一样
    * {{forloop.counter0}} 从零开始递增
    * {{forloop.revcounter}} 序号从大道小，即逆序
    * {{forloop.revcounter0}} 逆序从零开始
    * {{forloop.first}} 判断用，判断是否是序列的第一个
    * {{forloop.last}} 判断用，判断是否是序列的最后一个
    * {{forloop.parentloop}} 判断用，判断是否是上一次递归

## 使用模板的几种方式
导入```render_to_response```
>from django.shortcuts import render,render_to_response

>def index(req):
     title = {'user':'root','passwd':123456}
     return render_to_response('index1.html',{'title':title})

title是传递的模板变量，可以是普通变量，字典，对象等在html模板{}中可以写对象的属性，对象的方法，调用方法时不可以传参 ，不要写括号，必须有返回值

渲染时存在优先级问题:普通变量>字典>对象的属性>对象的方法>列表。
### 第二种方法
```
from django.shortcuts import render,render_to_response
from django.template import loader
from django.http import HttpResponse

def index1(req):
    t = loader.get_template('index1.html')  //加载模板
    title = {'user':'root','passwd':123456} //设置模板变量
    html = t.render(title)                  //渲染模板变量
    return HttpResponse(html)               //渲染html
```

### 第三种方法(这个好像没成功)
```
def index2(req):
    t = Teplate(' <h1>hello</h1> ')        //通过Template类创建一个模板
    title = {'user':'root','passwd':123456} //设置模板变量
    html = t.render(title)                  //渲染模板变量
    return HttpResponse(html)               //渲染html
```

## 通过urls.py文件向url方法里的index函数传递变量有两种方法。
+ get方法
+ 正则表达式分组 (?P<id>/d{2}) 这是一个分组 规定变量的形参名 ，调用方法要加上相同的行参名。 如果没有规定形参名(/d{2}),那么可以随意设置形参名即可


## Django模板标签

### ifequal/ifnotequal        //判断两个值是否相等
    {% ifequal user currentuser %}
    {% endif %}

## 注释
+ {# 这是个注释 #}
+     {% comment %}
    * {% endcomment %}

## 过滤器  {{name | lower}} 相关自行查询

## include 模板标签
+ 如果这个模板没有导入父模板的话，可以使用include标签。
+ 导入了父模板的模板是不能用include标签的。
+ include标签的使用
+ {% include '模板名称' %}    //模板名称可以是模板变量 可以写模板的相对位置‘template/模板名称’

## 模板继承
+ 在父模板中定义

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <h1>My helpful timestamp site</h1>
    {% block content %}{% endblock %}
    {% block footer %}
    <hr>
    <p>Thanks for visiting my site.</p>
    {% endblock %}
</body>
</html>    
```

> {% block %} 。 所有的 {% block %} 标签告诉模板引擎，子模板可以重载这些部分。
 每个{% block %}标签所要做的是告诉模板引擎，该模板下的这一块内容将有可能被子模板覆盖。 

 + 在子模版中使用

>{% extends "base.html" %}   //继承base.html 模板 必须写在最前面

>{% block title %}The current time{% endblock %}
>{% block content %}
>{{block.super}}       //这里可以使用{{block.super}}父模块中的内容 在进行更改，也就是添加一些内容
><p>It is now {{ current_date }}.</p>
>{% endblock %} 



## 模板的使用技巧

如果在模板中使用 {% extends %} ，必须保证其为模板中的第一个模板标记。 否则，模板继承将不起作用。
一般来说，基础模板中的 {% block %} 标签越多越好。 记住，子模板不必定义父模板中所有的代码块，因此你可以用合理的缺省值对一些代码块进行填充，然后只对子模板所需的代码块进行（重）定义。 俗话说，钩子越多越好。

如果你需要访问父模板中的块的内容，使用 {{ block.super }}这个标签吧，这一个魔法变量将会表现出父模板中的内容。 如果只想在上级代码块基础上添加内容，而不是全部重载，该变量就显得非常有用了。

不允许在同一个模板中定义多个同名的 {% block %} 。 存在这样的限制是因为block 标签的工作方式是双向的。 也就是说，block 标签不仅挖了一个要填的坑，也定义了在父模板中这个坑所填充的内容。如果模板中出现了两个相同名称的 {% block %} 标签，父模板将无从得知要使用哪个块的内容。

## locals()技巧

```
locals()返回一个包含当前作用域里面的所有变量和它们的值的字典

from django.shortcuts import render_to_response
import datetime
def current_datetime6(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime6.html', locals())
```

## Django模型
### 安装mysql 安装pymysql
> pip install pymysql

### 进行settings.py配置
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',   //将这里的.后面加上mysql
            'NAME': 'testpython',
            'USER':'root',
            'PASSWORD':'123456',
            'HOST':'',
            'PORT':'',
        }
    }

### blog/__init__.py配置
    import pymysql
    pymysql.install_as_MySQLdb()

### blog/models.py配置

    from django.db import models
    
    # Create your models here.
    class Employee(models.Model):             //创建一个表，Employee(表名)
        """docstring for Employee"""            
        # def __init__(self, arg):
        #   super(Employee, self).__init__()
        #   self.arg = arg
        name = models.CharField(max_length=20)    //创建一个字段，name(字段名称) 类型CharField(varchar),最大长度20
        //自动创建id字段，并为主键，自增
    
        def __str__(self):       
            return self.name
    
         //解码，返回name字段用于进行任何处理来返回对一个对象的字符串表示



### powershell下的项目文件夹下运行
+ 验证模型的有效性
    * > python manager.py check
+ 生成create table语句
    * > python manager.py makemigrations blog //app名称
+ 提交SQL语句至数据库
    * > python manager.py migrate
+ 创建管理员账户 python manager.py createsuperuser


## 在shell下添加、修改数据
> python manager.py shell

    from blog.models import Employee
    
    emp = Employee()    //
    emp.name = 'Alen'
    emp.save()
    
    emp = Employee(name = 'Tom')  //第二种，创建类时，传入参数
    emp.save()                    
    
    emp = Employee.object.create(name='Max')  //第三种方法调用object，不需要save()
    
    emps = Employee.object.all()    //查询所有的数据，存入emps中
    emps[0].id
    emps[0].name   

## 在views.py传递
>emps = Employee.objects.all()
>return render_to_response('index.html',locals())

## 一对多关系
    class Entry(models.Model):
        name = models.CharField(max_length=20)
        def __str__(self):
            return self.name
    class Blog(models.Model):
        name = models.CharField(max_length=20)
        entry = models.ForeignKey(Entry,on_delete=models.CASCADE)  //记得写第二个参数on_delete=models.CASCADE
        def __str__(self):
            return self.name

## 在shell中查看
    from blog.models import Entry.Blog
    entry1 = Entry.objects.create(name='alen')    //一个作者
    blog1 = Blog.objects.create(name='alen_blog1',entry=entry1)//可以写多篇文章
    blog2 = Blog.objects.create(name='alen_blog2',entry=entry1)
    blog3 = Blog.objects.create(name='alen_blog3',entry=entry1)
## 查看
    blog1.entry (输出)<Entry: alen>
    blog2.entry (输出)<Entry: alen>
    
    blog1.entry_id    (输出)out[20]: 1


    entry.blog_set.all()
     <QuerySet [<Blog: alen_blog1>, <Blog: alen_blog2>, <Blog: alen_blog3>]>(输出)

## python manager.py shell 下的增删改查

1、models.AutoField　　自增列 = int(11)
　　如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。
2、models.CharField　　字符串字段
　　必须 max_length 参数
3、models.BooleanField　　布尔类型=tinyint(1)
　　不能为空，Blank=True
4、models.ComaSeparatedIntegerField　　用逗号分割的数字=varchar
　　继承CharField，所以必须 max_lenght 参数
5、models.DateField　　日期类型 date
　　对于参数，auto_now = True 则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。
6、models.DateTimeField　　日期类型 datetime
　　同DateField的参数
7、models.Decimal　　十进制小数类型 = decimal
　　必须指定整数位max_digits和小数位decimal_places
8、models.EmailField　　字符串类型（正则表达式邮箱） =varchar
　　对字符串进行正则表达式
9、models.FloatField　　浮点类型 = double
10、models.IntegerField　　整形
11、models.BigIntegerField　　长整形
　　integer_field_ranges = {
　　　　'SmallIntegerField': (-32768, 32767),
　　　　'IntegerField': (-2147483648, 2147483647),
　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),
　　　　'PositiveSmallIntegerField': (0, 32767),
　　　　'PositiveIntegerField': (0, 2147483647),
　　}
12、models.IPAddressField　　字符串类型（ip4正则表达式）
13、models.GenericIPAddressField　　字符串类型（ip4和ip6是可选的）
　　参数protocol可以是：both、ipv4、ipv6
　　验证时，会根据设置报错
14、models.NullBooleanField　　允许为空的布尔类型
15、models.PositiveIntegerFiel　　正Integer
16、models.PositiveSmallIntegerField　　正smallInteger
17、models.SlugField　　减号、下划线、字母、数字
18、models.SmallIntegerField　　数字
　　数据库中的字段有：tinyint、smallint、int、bigint
19、models.TextField　　字符串=longtext
20、models.TimeField　　时间 HH:MM[:ss[.uuuuuu]]
21、models.URLField　　字符串，地址正则表达式
22、models.BinaryField　　二进制
23、models.ImageField   图片
24、models.FilePathField 文件

## 增删改查
    增
    
    models.Tb1.objects.create(c1='xx', c2='oo')  增加一条数据，可以接受字典类型数据 **kwargs

    obj = models.Tb1(c1='xx', c2='oo')
    obj.save()

    查
    
    models.Tb1.objects.get(id=123)         # 获取单条数据，不存在则报错（不建议）
    models.Tb1.objects.all()               # 获取全部
    models.Tb1.objects.filter(name='seven') # 获取指定条件的数据

    删
    
    models.Tb1.objects.filter(name='seven').delete() # 删除指定条件的数据

    改
    models.Tb1.objects.filter(name='seven').update(gender='0')  # 将指定条件的数据更新，均支持 **kwargs
    obj = models.Tb1.objects.get(id=1)
    obj.c1 = '111'
    obj.save()                                                 # 修改单条数据

基本操作---增删改查，增删改后，需要重新导入Employee类
[相关链接](http://www.cnblogs.com/luxiaojun/p/5795070.html)

## querySet的遍历
    emps = Employee.objects.all()
    for x in emps:
        print(x.id)    //x.字段名称  将所有的字段都打印出来
    
    emps = Employee.objects.all()
    emps.values()     //返回一个字典类型，所有的值，相当于select * from blog_Employee;
    
    也可以查询单个的值
    emps = Employee.object.filter(id=1).values() //查询id=1的所有值
    emps = Employee.object.filter(id=1).values('id','name') //查询id=1的id,name值



> from blog.models import Employee

     emp = Employee.objects.filter(id=1)
     print(emp.query)         #emp.query 转变为SQL语法格式
     [out]: SELECT `blog_employee`.`id`, `blog_employee`.`name`, `blog_employee`.`age`, `blog_employee`.`addr` FROM `blog_employee` WHERE `blog_employee`.`id` = 1   # 这里是转变完的

## admin后台管理。
### 创建项目 django-admin.exe startproject csvt
### 创建一个应用 django-admin.exe startapp blog
### 在blog文件夹下创建一个名为templates的文件夹，并在该文件夹下创建一个index1
### settings.py设置，导入应用，'DIRS': [os.path.join(BASE_DIR, 'templates')]，在MIDDLEWARE =[]中添加'django.middleware.locale.LocaleMiddleware',这句意思后台采用中文。
### urls.py设置
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = [
        # path('admin/', admin.site.urls),
        url(r'^admin/',admin.site.urls),
        url(r'^blog/regist/$',register),
        # url(r'^blog/regist/test/$',register)
    ]
### admin.py设置
    from django.contrib import admin
    from blog.models import User  #models的User表
    # Register your models here.
    class UserAdmin(admin.ModelAdmin):  
        list_display = ('name','age',)#列表显示
        # list_per_page = 50                             #列表每页显示多少条信息
        # list_display_links = ('name',)                   #列表可编辑字段
        # list_editable = ['name',]
        # search_fields = ('name','age','sex',)     #可以查询的字段，增加查询框
        # list_filter = ('name','age','sex',)                   #查询的结果在进行过滤的过滤器，增加过滤框
        # date_hierearchy = 'pub_date'                      
        # ordering = ('-pub_date',)             #列表按照这些字段依次进行排序，逆序在前

    admin.site.register(User,UserAdmin)

## Django 多对多关系模型
### models.py配置
    from django.db import models
    
    sex_choices = (
        ('f','female'),
        ('m', 'male'),
    )
    
    class Author(models.Model):
        name = models.CharField(max_lenght=20)
        sex = models.CharField(max_length=1,choices=sex_choices)
        # pub_date = models.DateTimeField(auto_now_add=True) 自动添加时间，创建时添加
    
    class Book(models.Model):
        name = models.CharField(max_length=20)
        author = models.ManyToManyField(Author)  ##多对多
    
        def __str__(self):
            return self.name
### shell 下查询
    alen = Author.object.get(name='alen')
    alen.book_set.all()    #获取Alen所有的书
    alen.book_set.add(Book对象)  #向alen中添加书籍
    alen.book_set.create(name='book1')  #创建一本书，并添加到alen中，book表里也新建了这本书

    book1 = Book.object.get(name='book1')
    book1.author.all()   #获取这本书的所有作者
    book1.author.add(Author对象) #添加一个作者
    book1.author.remove(Author对象) #删除一个作者
    book1.author.create(name='Bob')#创建一个作者，并添加到book1中，Author表中新建一个Bob对象






