from django.conf.urls import patterns, include, url
from django.contrib import admin
from open_news import views
from open_news.views import News
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	#url(r'^$', 'example_project.views.home', name='home'),
    #url(r'^example_project/', include('example_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	# url(r'^notes/', views.ArticleDetailView, name='article-detail'),
	
	url(r'^indexed/', views.indexed, name='indexed'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^tested/', views.tested, name='tested'),
	url(r'^cover/', views.cover, name='cover'),
	url(r'^$', views.get_name, name='get_name'),
	url(r'^thanks/', views.thanks, name='thanks'),
	url(r'^search/', views.search, name='search'),
	url(r'^form_upload/',views.post_form, name='post_form'),
	url(r'^perms/', views.user_gains_perms, name='perms'),
	url(r'^publishers/$', News.as_view(), name='publishers'),
	#url(r'^display_news/', views.news, name ='news'),
	url(r'^comments/', include('django_comments.urls')),
	url(r'^login/$', views.my_view, name='my_view'),
	
	
	
	
)
