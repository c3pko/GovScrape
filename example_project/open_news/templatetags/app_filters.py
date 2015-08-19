from django import template
register = template.Library()

@register.filter(name='get_title', 'get_desc', 'get_url')
def get_title(value):
	from open_news.models.Article return Article.title
def get_desc(value):
	return "hello"
	
	
def get_url(value):
	from open_news.models.Article return Article.newswebsite