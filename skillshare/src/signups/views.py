#python first
#djangp second
#your apps
#local directory

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.

from .forms import SignUpForm
from django import forms
from django.forms import ModelForm
from .models import *

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=120)
	password = forms.CharField(label='Password', max_length=120, widget=forms.PasswordInput)
	
class TestimonialForm(ModelForm):
	class Meta:
		model = Testimonial
		fields = ['first_name', 'last_name', 'city', 'state', 'message']
	# first_name = forms.CharField(label='First name', max_length=120)
	# last_name = forms.CharField(label='Last name', max_length=120)
	# city = forms.CharField(label='City', max_length=120)
	# state = forms.CharField(label='State', max_length=120)
	# message = forms.CharField(label='Message', max_length=300)


def vwap(some_view):
	
	# wrapper just sets the username for the nav bar if logged in
	def inner(request):
		username = ""
		if request.user.is_authenticated():
			username = request.user.username
		return some_view(request, username)
	return inner

@vwap
def home(request, username):
	
	return render_to_response("signup.html",
								locals(),
								context_instance=RequestContext(request))
@vwap	
def thankyou(request, username):
	form = SignUpForm(request.POST or None)
	
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		subject = 'Thank you for your Pre-Order from us!'
		message = 'Welcome to the dark side.\nI appreciate your interest in the dark side.'
		from_email = settings.EMAIL_HOST_USER
		to_list = [save_it.email, settings.EMAIL_HOST_USER]
		send_mail(subject, message, from_email, to_list, fail_silently=True)
		messages.success(request, 'Thank you for your order. We will be in touch.')
		return HttpResponseRedirect('/thank-you/')
	
	
	return render_to_response("thankyou.html",
								locals(),
								context_instance=RequestContext(request))
@vwap	
def testimonials(request, username):
	form = TestimonialForm(request.POST or None)
	
	if form.is_valid():
		save_it = form.save()
		save_it.save()
		message = request.POST.get('first_name')
		messages.success(request, 'Thank you for the feedback.')
	else:
		messages.success(request, 'Please fill out every field.')
	
	# html inject this stuff into a table if approved
	output = Testimonial.objects.all();
	
	
	return render_to_response("testimonials.html",
								locals(),
								context_instance=RequestContext(request))


@vwap
def aboutus(request, username):
	return render_to_response("aboutus.html",
								locals(),
								context_instance=RequestContext(request))
@vwap
def services(request, username):
	return render_to_response("services.html",
								locals(),
								context_instance=RequestContext(request))
@vwap	
def signin(request, username):
	
	password = ''
	# form = LoginForm(request.POST or None)
	form = LoginForm(request.POST or None)
	# if form.is_valid():
	# username = request.POST['username']
	# password = request.POST['password']
	# user = authenticate(username=form.user_name, password=form.password)
	# if user is not None:
	# 	if user.is_active:
	# 		login(request, user)
	# 		return HttpResponseRedirect('/logged-in/')
	# 	else:
	# 		messages.success(request, 'Thank you for your order. We will be in touch.')
	# 		return HttpResponseRedirect('/sign-in/')
	
	
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You've been logged in!"
				messages.success(request, 'Login successful!')
				return HttpResponseRedirect('/')
			else:
				messages.success(request, 'Failed login, contact admin.')
		else:
			messages.success(request, "Incorrect username and or password.")
			
	return render_to_response("signin.html",
								locals(),
								context_instance=RequestContext(request))
@vwap	
def createaccount(request, username):
	
	return render_to_response("createaccount.html",
								locals(),
								context_instance=RequestContext(request))

@vwap
def loggedout(request, username):
	
	
	# # if request.GET:
	# logout(request)
	# messages.tags = ""
	# # return HttpResponseRedirect('/thank-you/')
	
	return render_to_response("loggedout.html",
								locals(),
								context_instance=RequestContext(request))