import scrapy
import json


class IteSpider(scrapy.Spider):
    name = 'ite'
    allowed_domains = ['www.ite.edu.sg']
    start_urls = ['http://www.ite.edu.sg/']

    def parse(self, response):
        #below code
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page),callback=self.parse)
        css_selector = 'jpg'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'image Link': x.xpath(newsel).extract_first(),
            }
            # a = '''{
            #     'imageUrl':'/images/image.jpg',
            #     'imageName': 'My Image'
            # }'''
            # decoded = json.loads(a)
            # img = scrapy.urlopen(decoded.imageUrl).read()

with open('results.json', 'r') as f:
    f = '''{
      'imageUrl': '/images/image.jpg',
      'imageName': 'My Image'  
    }'''
    results_dict = json.load(f)
    img = scrapy.urlopen(results_dict.imageUrl).read()

for results in results_dict:
    print(results['Name'])
