from scraper import *

#to execute : scrapy runspider scraper.py

class BrickSetSpider(scrapy.Spider):
	name = "brickset_spider"
	start_urls = ['http://brickset.com/sets/year-2016']