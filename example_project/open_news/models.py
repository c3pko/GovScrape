from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy.contrib.djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
'''
attempt at a userprofile auth class with a 'favorite_animal' codename

class UserProfile(models.Model):
	
	user = models.OneToOneField(User)
	
	accepted_eula = models.BooleanField()
	favorite_animal = models.CharField(max_length=20, default="Dragons.")
	user = authenticate(username='nstcr', password='Drag0nS')
	if user is not None:
		if user.is_active:
			print("User is valid, activate and authenticated")
		else:
			print("The password is valid, but the account has been disabled!")
	else:
		print("The username and password were incorrect.")
		

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)
		
	post_save.connect(create_user_profile, sender=User)
'''

class Person(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	codename = models.CharField(max_length=100)
	
	
	
	
class NewsWebsite(models.Model):
    name = models.CharField(max_length=600)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=600)
    news_website = models.ForeignKey(NewsWebsite) 
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    thumbnail = models.CharField(max_length=300, blank=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.title


class ArticleItem(DjangoItem):
    django_model = Article


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, NewsWebsite):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()
    
    if isinstance(instance, Article):
        if instance.checker_runtime:
            instance.checker_runtime.delete()
            
pre_delete.connect(pre_delete_handler)