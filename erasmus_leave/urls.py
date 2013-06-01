from django.conf.urls import patterns, url

from erasmus_leave import views

urlpatterns = patterns('',
#	url(r'^$', views.index, name='index'),
#	url(r'^(?P<osoba_id>\d+)/$', views.detail, name='detail'),
#   url(r'^(?P<osoba_id>\d+)/results/$', views.results, name='results'),


	url(r'^(?P<osoba_id>\d+)/updateosoba/$', views.updateosoba, name='updateosoba'),
	
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^time/$', views.current_datetime, name='time'),
	url(r'^(?P<osoba_id>\d+)/updateosoba/$', views.updateosoba, name='updateosoba'),
	url(r'^osobaform/$', views.osobaform, name='osobaform'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^(?P<osoba_id>\d+)/osoba_editform/$', views.osoba_editform, name='osoba_editform'),
	url(r'^osoby/$', views.OsobaList.as_view()),
)
