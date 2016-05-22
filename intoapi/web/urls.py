from django.conf.urls import url
from django.contrib.auth import views as auth
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^login/$', auth.login, name='login', kwargs={'template_name': 'web/login.html'} ),
    url(r'^logout/$', auth.logout, name='logout', kwargs={'next_page': '/login/'} ),
    
    url(r'^events/$', views.events, name='events'),
    url(r'^events/(?P<event_id>[0-9]+)/$', views.single_event, name='single_event'),
    url(r'^events/(?P<event_id>[0-9]+)/products/$', views.event_products, name='event_products'),
    url(r'^events/(?P<event_id>[0-9]+)/guests/$', views.guests, name='guests'),
    url(r'^events/(?P<event_id>[0-9]+)/guests/(?P<guest_id>[0-9]+)/products$', views.guest_products, name='guest_products'),
    
]
