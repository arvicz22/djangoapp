from django import forms
from django.forms import ModelForm
from .models import *

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=120)
	password = forms.CharField(label='Password', max_length=120, widget=forms.PasswordInput)
	
class TestimonialForm(ModelForm):
	
	class Meta:
		model = Testimonial
		fields = ['first_name', 'last_name', 'city', 'state', 'message']