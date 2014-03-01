from django.contrib import admin

# Register your models here.
from .models import SignUp
from .models import Testimonial

class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp
		
class TestimonialAdmin(admin.ModelAdmin):
	class Meta:
		model = Testimonial

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Testimonial, TestimonialAdmin)