from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
    url(r'^$', 'signups.views.home', name='home'),
	url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
	url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
	url(r'^services/$', 'signups.views.services', name='services'),
	url(r'^testimonials/$', 'signups.views.testimonials', name='testimonials'),
	url(r'^sign-in/$', 'signups.views.signin', name='signin'),
	url(r'^logged-out/$', 'signups.views.loggedout', name='loggedout'),
	url(r'^log-out/$', 'django.contrib.auth.views.logout', {'next_page': 'loggedout'}, name='logout'),
	url(r'^create-account/$', 'signups.views.createaccount', name='createaccount'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
							document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)