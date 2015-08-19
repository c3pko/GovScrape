import scrapy
from scrapy.item import Item, Field


class Website(Item):

    title = Field()
    description = Field()
    link = Field()

class DmozItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()