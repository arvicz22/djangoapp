from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class SignUp(models.Model):
	for_you = models.BooleanField(default=True, verbose_name="Is this purchase for you? If so, check this box.")
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
		return smart_unicode(self.first_name)

class Testimonial(models.Model):
	class Meta:
		app_label = "signups"
	
	def is_valid():
		if all(x is not None for x in [first_name, last_name, city, state, message]):
			return True
		return False	
	
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	city = models.CharField(max_length=120, null=True, blank=True)
	state = models.CharField(max_length=120, null=True, blank=True)
	message = models.CharField(max_length=300, null=True, blank=True)
	approved = models.BooleanField(default=False, verbose_name="Approved by admin.")
	# timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	def __unicode__(self):
		return smart_unicode(self.message)