# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/113652/']

    def parse(self, response):
        # re_seletor = response.xpath('//div[@class="enrty-header"/h1]')
        # print(re_seletor)
        title = response.css('.entry-header h1::text').exltract()
        create_date =response.css('p.entry-meta-hide-on-mobile::text').extract()[0].strip().replace('·','').strip()
        praise_num = response.css('.vote-post-up h10::text').extract()[0]

        pass
 
