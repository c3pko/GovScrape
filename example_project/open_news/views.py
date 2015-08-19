from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404, render
from .forms import UserForm, PostForm, Com
from open_news.models import NewsWebsite, Article, ArticleItem, Person
from django.core.exceptions import *
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils import timezone
from 

from django.core.management import call_command
import sys
stdout_backup, sys.stdout = sys.stdout, open('output_file', 'w+')
call_command('govtrackcommand')
sys.stdout = stdout_backup
'''
from open_news.management.commands import govtrackcommand
//govtrackcommand is a one off python command
//if someone could deploy it with views and that is easier
//than django scrapy scraping, then do it.
'''

def view_bills(request):
	call_command('govtrackcommand')

	'''bill_info = Bills()
	b = bill_info.get_bill_fields()
	'''
	return render(request, 'bi.html')
	#return bills

class News(ListView):

	model = Article
	
	template_name = 'news.html'
	queryset = Article.objects.filter(news_website=1)
	
	def get_context_data(self, **kwargs):
		context = super(News, self).get_context_data(**kwargs)
		context['title'] = Article.objects.all()
		return context
	

class ArticleDetailView(DetailView):
	model = ArticleItem
	def get_context_data(self, **kwargs):
		context = super(ArticleDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

		
		
def indexed(request):
	model = Person
	
	if request.method== 'POST':
		form = Com(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/admin/')
	else:
		form=Com()
	return render(request, 'pie.html', {'form':form})
	
	
		
def post_form(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			comment = form.cleaned_data['comment']
			name = form.cleaned_data['name']
			post = m.Post.objects.create(comment=comment,name=name)
			
			return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
	else:
		form =UserForm()
	return render(request, 'post_form_upload.html', {'form':form})

#@login_required(redirect_field_name='cover')
def get_name(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username='nstcR', password='1967R')
		if user is not None:
			if user.is_active:
				login(request,user)
				print("User is valid, active and authenticated")
				return HttpResponseRedirect('perms/')
			else:
				return HttpResponseRedirect('/index')				
				print("The password is vlaid, but the account has been disabeled!")
		else:
			print("The username and password were incorrect.")
		#redirect to user_gains_perms page
	else:
		form=UserForm()
	return render(request, 'post_form_upload.html', {'form':form})
	
'''def user_gains_perms(request, user_id):
	
	
	user=get_object_or_404(User, pk=user_id)
    user.has_perm('open_news.change_bar')
    permission = Permission.objects.get(codename='change_bar')
    user.user_permissions.add(permission)
	user.has_perm('open_news.change_bar')
    user = get_object_or_404(User, pk=user_id)
    user.has_perm('open_news.change_bar')
	
	return HttpResponseRedirect('/admin')
'''	


def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = Person.objects.get(name = search_id)
            #do something with user
            html = ("<H1>%s</H1>", user)
            return HttpResponse(html)
        except Person.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'form.html')
		

def thanks(request):
	return HttpResponse("Thank you for signing in")
	return HttpResponseRedirect('/admin')
	
	
def cover(request):
	
	cov = get_template('cover.html')
	c = cov.render(Context({'cover': cov}))
	
	return HttpResponse("hello")
	

def tested(request):
	
	t = get_template('tested.html')
	tex = t.render(Context({'tested':t}))
	return HttpResponse(tex)

def my_view(request):

	model = Person
	username=request.POST.get('username')
	password=request.POST.get('password')
	
	user = authenticate(username=username, password=password)
	
	if user.is_valid:
		return HttpResponseRedirect('/admin/')
		
		
	#profile = request.user.get_profile()
	
	
'''another attempt at specifying user_permissions access'''

def user_gains_perms(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	user.has_perm('open_news.change_bar')
	
	user.has_perm('open_news.change_bar')
	user=get_object_or_404(User, pk=user_id)
	user.has_perm('open_news.change_bar')
	
	
	