from scrapy import spiders

class BiliSpider(spiders.Spider):
	"""docstring for BiliSpider"""
	
	name = 'bili'
	allowed_domains = ['bili.org']

	start_urls = [
		'https://bangumi.bilibili.com/anime/21466',
	]

	# def __init__(self, arg):
	# 	super(BiliSpider, self).__init__()
	# 	self.arg = arg
	def parse(self,response):
		# filename = response.url.splite('')[-2]
		# with open(filename,'wb') as f:
		# 	f.write(response.body)
		for sel in response.xpath('//ul/li'):
			title = sel.xpath('a/text()').extract()
			link = sel.xpath('a/@href').extract()
			desc = sel.xpath('text()').extract()
			print(title,link,desc)


