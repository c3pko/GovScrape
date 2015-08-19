from django import forms


class UserForm(forms.Form):
	username = forms.CharField(label="username",max_length=50)
	password = forms.CharField(label="password",max_length=50)

class PostForm(forms.Form):
	comment = forms.CharField(max_length=250)
	name = forms.CharField(max_length = 50)
	
class Com(forms.Form):
	
	content = forms.CharField(max_length=200)
	
	