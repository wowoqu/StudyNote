## Python WebScrap
### 相关框架
+ urllib
+ requests
+ scrapy
+ BeautifulSoup

### 一个简单的爬虫程序
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    html = urlopen('http://www.pythonscraping.com/pages/page1.html') #获取页面html对象
    bsobj = BeautifulSoup(html.read(),'lxml')  
    #执行html.read()后，html将没有内容 
    #BeautifulSoup()可以直接绑定html对象
    BeautifulSoup(html,'lxml')
    #获取页面内容html.read(),并以'lxml'解析器标准化
    print(bsobj) #打印整个页面
    print(bsobj.title) #打印页面的标题包含<title></title>，如果只是打印内容的话用bsobj.title.get_text()获取

### 添加异常处理
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    from urllib.request import HTTPError,URLError
    
    def getTitle(url):
        try:
            html = urlopen(url)
        except (HTTPError,URLError) as e:
            return None
        try:
            bsobj = BeautifulSoup(html.read(),'lxml')
            title = bsobj.body.h1
        except AttributeError as e:
            return None
    
    #调用
    title = getTitle('http://www.pythonscraping.com/pages/page1.html')
    if title == None:
        print('Title could not be found')
    else:
        print(title)
### BeautifulSoup的find(),findAll()
+ find()，findAll(tag,attributes,recursive,text,limit,keywords)
    * find(tag,attributes,recursive,text,keywords)
    * find('h1',{'class':'text'},recursive=True,text='abc',id='b')
    * attributes,用字典封装标签的若干属性和对应的值{'class':{'abc','def'}}
    * recursive设置为True，会查找标签参数的所有子标签，默认为True
    * find(),相当于findAll()的limit=1
    * text,用标签的文本内容去匹配，而不是用标签的属性
    * keyword，让你选择那些具有指定的标签


### 处理子标签和兄弟标签
bsobj.find('table',{'id':'abc'}).children   #获取指定标签的所有子标签，不包括孙子标签
bsobj.find('table',{'id':'abc'}).tr.next_siblings 
# 获取指定标签的同级向下的所有兄弟标签，不包括向上的标签
bsobj.find('table',{'id':'abc'}).tr.previous_siblings
# 指定标签的同级向上的所有兄弟标签
bsobj.find('table',{'id':'abc'}).parent  #父级标签

## 正则表达式
\* 匹配前面的字符、子表达式、或括号里的字符0次或多次
\+ 匹配前面的字符、子表达式、或括号里的字符至少一次
\[\] 匹配任意一个字符，相当于任选一个 \[A-Z\]\*
() 表达式编组
{m,n} 匹配前面的字符、子表达式、或括号里的字符m到n次
\[^\] 匹配任意一个不在中括号里的字符
| 匹配任意一个由竖线分割的字符、子表达式 b(a|b|c)d
. 匹配任意单个字符（包括符号，数字和空格等）

### 正则实例
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import re
    
    html = urlopen('http://www.pythonscraping.com/pages/page3.html')
    bsobj = BeautifulSoup(html.read(),'lxml')
    images = bsobj.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
    for image in images:
        print(image['src'])  #获取属性的值


### 遍历单个域名
    from urllib.requests import urlopen
    from bs4 import BeautifulSoup

    html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
    bsobj = BeautifulSoup(html.read(),'lxml')
    for link in bsobj.findAll('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])
    

### 页面随机跳转到子链接，直到不再有子链接为止
    from urllib.requests import urlopen
    from bs4 import BeautifulSoup
    import datetime
    import random
    import re
    
    random.seed(datetime.datetime.now())  #将当前时间设置为随机种子
    def getLinks(articleUrl):
        html = urlopen('http://en.wikipedia.org' + articleUrl)
        bsobj = BeautifulSoup(html,'lxml')
        return bsobj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)(?!:).)*$'))
    links = getLinks('/wiki/Kevin_Bacon')
    while len(links) >0 :
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
    

### 采集整个网站
    from urllib.requests import urlopen
    from bs4 import BeautifulSoup
    import re
    
    pages = set()
    def getLinks(pageUrl):
        global pages
        html = urlopen('http://en.wikipedia.org'+pageUrl)
        bsobj = BeautifulSoup(html)
        for link in bsobj.findAll('a',href=re.compile('^(/wiki/)')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)
    getLinks('')     #从站点根目录开始

# 以下为Python Scripy内容
爬虫的目的将非结构性语言转换为结构性语言
## 案例一：Jobbole网站爬取 
### 创建虚拟环境 (可能不是完整的)

创建环境

>mkvitrutualenv --python=这里填写python版本所在的位置\python.exe article_spider(虚拟环境名称)

安装scripy：

>pip install -i https://pypi.douban.com/simple/ scripy

进入虚拟环境：

>workon article_spider

安装pypiwin32
>pip install -i https://pypi.duoban.com/simple/ pypiwin32

新建工程：

>scrapy startproject Articlespider

进入工程：

>cd ArticleSpider

创建基于basic模板

>scrapy genspider jobbole blog.jobbole.com //生成jobbole.py文件

jobbole.py
    
    import scrapy                        //导入scrapy
    class JobboleSpider(scrapy.Spider):  //创建类继承scrapy.Spider
        name = 'jobbole'                 //爬虫名称
        allowed_domains = ['blog.jobbole.com']  //爬取域名
        start_urls = ['http://blog.jobbole.com/all-posts/']
        //爬取地址
        def parse(self, response):       //爬取入口函数
            pass

写一个自己的main文件，调用命令行，进行debug，不用每次都在命令行执行scrapy crawl jobbole
main.py

    from scrapy.cmdline import execute
    
    import sys
    import os
    
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))  //获取当前路径
    
    execute(['scrapy','crawl','jobbole'])

更改setting
>ROBOTSTXT_OBEY = False //取消遵守robots协议

用debug或者cmd中的shell脚本调试获取网页标签的值是否正确
shell脚本：
>scrapy shell 网站地址

添加爬取字段：

    def parse_datail(self,response):
        //获取爬取字段
        title = response.css('.entry-header h1::text').extract()
        create_data = response.css('p.entry-meta-hide-on-mobile::text').extract_first('')
        content = response.css('div.entry').extract_first()

    def parse(self, response):
    """
    1.获取文章列表中的文章url并交给scrapy下载后并进行解析
    2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse
    :param response:
    :return:
    """

    # 解析列表页中的所有文章url并交给scrapy下载后进行解析
    post_nodes = response.css('#archive .floated-thumb .post-thumb a')
    for post_node in post_nodes:
        # Request(url=post_url, callback=self.parse_detail)
        # print(post_url)
        image_url = post_node.css('img::attr(src)').extract_first('')
        post_url = post_node.css('::attr(href)').extract_first('')
        #返回给scrapy进行下载，callback执行提取爬取字段函数
        #通过Request()函数返回，并异步调用获取爬取字段函数，request.meta变量用来传递参数
        yield Request(url=parse.urljoin(response.url,post_url),meta={'front_image_url':image_url},callback=self.parse_detail)
    #提取下一页并进行下载
    next_url = response.css('.next.page-numbers::attr(href)').extract_first('')
    if next_url:
        yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)
    else:
        pass

items.py用来保存爬取的字段并路由到pipeline中

    import scrapy
    class ArticleItem(scrapy.Item):
        title = scrapy.Field()      //item只有Field()一种类型
        create_data = scrapy.Field()
        content = scrapy.Field()
        url = scrapy.Field()
        # url_object_id = scrapy.Field()
        # front_image_url = scrapy.Field()
        # front_image_path = scrapy.Field()

jobbole.py中导入创建的AritcleItem()

    from ArticleSpider.items import ArticleItem

在parse_detail()函数中创建实例并赋值

    def parse(self, response):
        ...
        article_item = ArticleItem()
        article_item['url_object_id'] = get_md5(response.url)
        article_item['title'] = title
        article_item['url'] = response.url
        article_item['create_data'] = create_data
        #article_item['front_image_url'] = [front_image_url]  //这里需要是数组
        article_item['content'] = content
        yield article_item   
        //这里需要使用yield返回创建的实例，然后会路由到pipeline中

通过Request传递当前爬取页面上一层页面数据到当前页面

    post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            # Request(url=post_url, callback=self.parse_detail)
            # print(post_url)
            #获取当前页面信息，image_url
            image_url = post_node.css('img::attr(src)').extract_first('')
            post_url = post_node.css('::attr(href)').extract_first('')
            #返回给scrapy进行下载，callback执行提取爬取字段函数
            #通过meta参数传递数据
            yield Request(url=parse.urljoin(response.url,post_url),meta={'front_image_url':image_url},callback=self.parse_detail)

接收数据

     def parse_detail(self, response):
        ...
        front_image_url = response.meta.get('front_image_url','')  
        //使用get方法获取，第二个参数是默认值

添加到AritcleItem()中：

    import scrapy
    class ArticleItem(scrapy.Item):
        title = scrapy.Field()      //item只有Field()一种类型
        create_data = scrapy.Field()
        content = scrapy.Field()
        url = scrapy.Field()
        # url_object_id = scrapy.Field()
        front_image_url = scrapy.Field()
        # front_image_path = scrapy.Field()

在parse_detail()中赋值

    def parse_datail(self,response):
        ...
        article_item['front_image_url'] = [front_image_url]  //这里需要是数组

    

通过settings.py启用pipelines

    ITEM_PIPELINES = {
    # 'ArticleSpider.pipelines.JsonWithEncodingPipeline': 2,
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    # 'ArticleSpider.pipelines.ArticleImagePipeline': 1,
    'ArticleSpider.pipelines.MysqlTwistedPipeline': 1,
    //第二个参数为优先级。
    }

安装pillow

>pip install pillow

使用scrapy.pipelines.images.ImagesPipeline模块下载图片

    ITEM_PIPELINES = {
    ...
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    }
    #设置选取字段
    IMAGES_URLS_FIELD = 'front_image_url'
    #设置保存路径(当前目录下的images文件夹)
    project_dir = os.path.abspath(os.path.dirname(__file__))
    IMAGES_STORE = os.path.join(project_dir, 'images')
    #设置图片过滤最小宽高
    IMAGES_MIN_WIDTH = 100
    IMAGES_MIN_HEIGHT = 100


自定义图片下载保存pipeline

在items.py中添加字段
items.py

    class ArticleItem(scrapy.Item):
        ...
        front_image_path = scrapy.Field()
    

pipelines.py

    class ArticleImagePipeline(ImagesPipeline): //继承系统ImagesPipeline
    #重写item_completed函数
    def item_completed(self, results, item, info):
        #获取并设置item['front_image_path']值
        for ok, value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item

更改settings.py配置

    ITEM_PIPELINES = {
    # 'ArticleSpider.pipelines.JsonWithEncodingPipeline': 2,
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    'ArticleSpider.pipelines.ArticleImagePipeline': 1,
    # 'ArticleSpider.pipelines.MysqlTwistedPipeline': 1,
    //第二个参数为优先级。
    }

将url通过md5转换一下
创建utils文件夹 创建common.py文件

    import hashlib
    
    def get_md5(url):
        if isinstance(url,str):
            url = url.encode('utf-8')  #函数不接受unicode，要先转化为utf-8
        m = hashlib.md5()
        m.update(url)
        return m.hexdigest()

jobbole.py
    
    from ArticleSpider.utils.common import get_md5
    
    def parse_detail(self, response):
        article_item['url_object_id'] = get_md5(response.url)

## 设计数据库并将Item保存到数据库中 

创建与item中对应的数据库表

pipelines.py

    class MysqlPipeline(object):
        # 此种方法为同步执行，效率较慢
        def __init__(self):
            self.conn = pymysql.connect('localhost', 'root', '123456', 'testpython', charset='utf8', use_unicode=True)
            self.cursor = self.conn.cursor()
        
        def process_item(self, item, spider):
            insert_sql = """
                insert into sex(mv_type,create_data,create_time,title)
                values (%s, %s, %s, %s)
            """
            try:
                self.cursor.execute(insert_sql, (
                    item['mv_type'], item['create_data'], item['create_time'], item['title']))
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()
    
        def spider_closed(self, spider):
            self.conn.close()
            self.cursor.close()




将item中的数据以json文件形式保存起来

    import codecs
    import json
    
    class JsonWithEncodingPipeline(object):
        # 自定义json保存
        def __init__(self):
            #类似于open
            self.file = codecs.open('article.json', 'w', encoding='utf-8')
        #重载process_item函数，启动时执行
        def process_item(self, item, spider):
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file.write(lines)
            return item
        #重载spider_closed()函数，当执行完成时，调用。是信号量
        def spider_closed(self, spider):
            self.file.close()

调用scrapy提供的json export导出json文件

    class JsonExporterPipeline(object):
        # 调用scrapy提供的json export导出json文件
        def __init__(self):
            self.file = open('articleexport.json', 'wb')
            self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
            self.exporter.start_exporting()
    
        def close_spider(self, spider):
            self.exporter.finish_exporting()
            self.file.close()
        #close_spider()是在满足一定条件时停止，而spider_closed()是当停止之后执行的代码，两者都可以实现相同作用。在这里一样
        def process_item(self, item, spider):
            self.exporter.export_item(item)
            return item


通过ItemLoader加载item(缺点：返回值都是list，每个都要写output_processor)

    #导入
    from scrapy.loader import ItemLoader
        def parse_detail(self,response):
            #创建ItemLoader实例，item必须加括号，为实例
            item_loader = ItemLoader(item=SeximageItem(),response=response)
            item_loader.add_css('title','.movieInfoList li.title::text')
            item_loader.add_css('mv_type','.movieInfoList li.title::text')
            item_loader.add_css('create_data','.movieInfoList li:nth-child(3)::text')
            item_loader.add_css('create_time','.movieInfoList li:nth-child(3)::text')
            #加载itemloader
            sexitem = item_loader.load_item()
            yield sexitem  

更改item，做预处理函数，设置返回值是数组第一个

    class SeximageItem(scrapy.Item):
        title = scrapy.Field(
            # input_processor = MapCompose(add_jobbole),  #添加多个处理函数
            # output_processor = TakeFirst()              #设置返回数组第一个
        )
        mv_type = scrapy.Field()
        # image_url = scrapy.Field()
        create_data = scrapy.Field(
            input_processor = MapCompose(data_convet)
        )
        create_time = scrapy.Field(
            input_processor=MapCompose(time_convet)
        )
        # vedio_url = scrapy.Field()
        # pass


创建自定义ItemLoader

    class SexItemLoader(ItemLoader):
        default_output_processor = TakeFirst()   #设置默认返回数组第一个，不用在每一个项中写入

items.py

    import scrapy
    import datetime
    from scrapy.loader.processors import MapCompose,TakeFirst
    from scrapy.loader import ItemLoader
    
    def add_jobbole(value):
        return value + 'jobbole'
    
    def data_convet(value):
        # value = value.split()[0]
        try:
            create_data = datetime.datetime.strptime(value,'%Y/%m/%d %H:%M:%S').date()
        except Exception as e:
            create_data = datetime.datetime.now().date()
        return create_data
    
    def time_convet(value):
        # value = value.split()[1]
        try:
            create_time = datetime.datetime.strptime(value, '%Y/%m/%d %H:%M:%S').time()
        except Exception as e:
            create_time = datetime.datetime.now().time()
        return create_time
    
    #自定义ItemLoader
    class SexItemLoader(ItemLoader):
        default_output_processor = TakeFirst()
    
    
    class SeximageItem(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        title = scrapy.Field(
            # input_processor = MapCompose(add_jobbole),  #添加多个处理函数
            # output_processor = TakeFirst()
        )
        mv_type = scrapy.Field()
        # image_url = scrapy.Field()
        create_data = scrapy.Field(
            input_processor = MapCompose(data_convet)
        )
        create_time = scrapy.Field(
            input_processor=MapCompose(time_convet)
        )
        # vedio_url = scrapy.Field()
        # pass


更改parse_detail

    #导入
    from scrapy.loader import ItemLoader
        def parse_detail(self,response):
            #创建SexItemLoader实例，item必须加括号，为实例
            item_loader = SexItemLoader(item=SeximageItem(),response=response)
            item_loader.add_css('title','.movieInfoList li.title::text')
            item_loader.add_css('mv_type','.movieInfoList li.title::text')
            item_loader.add_css('create_data','.movieInfoList li:nth-child(3)::text')
            item_loader.add_css('create_time','.movieInfoList li:nth-child(3)::text')
            #加载itemloader
            sexitem = item_loader.load_item()
            yield sexitem  

# Selenium Note

安装selenium

> pip install selenium











Tips:
>[element for element in tag_list if not element.strip().endswith('评论')] 
//返回不是以'评论'结尾的tag_list数组中的其他值，即将'评论'过滤掉
//相当于一个代码块 返回代码块开头的变量
