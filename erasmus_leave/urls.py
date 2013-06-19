from django.conf.urls import patterns, url
from erasmus_leave import views
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^erasmus_leave/', include('erasmus_leave.urls', namespace="erasmus_leave")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$',views.logout_page),
    url(r'^(?P<osoba_id>\d+)/updateosoba/$', views.updateosoba, name='updateosoba'),
	url(r'^$','django.contrib.auth.views.login'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^time/$', views.current_datetime, name='time'),
	url(r'^(?P<osoba_id>\d+)/updateosoba/$', views.updateosoba, name='updateosoba'),
	url(r'^osobaform/$', views.osobaform, name='osobaform'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^(?P<osoba_id>\d+)/osoba_editform/$', views.osoba_editform, name='osoba_editform'),
	url(r'^osoby/$', views.OsobaList.as_view()),
	

)
