from django.conf.urls import patterns, url

from erasmus_leave import views

urlpatterns = patterns('',
	#ex: /erasmus_leave/
	url(r'^$', views.index, name='index'),
	#ex: /erasmus_leave/5
	url(r'^(?P<osoba_id>\d+)/$', views.detail, name='detail'),
	# ex: /polls/5/results/
	#url(r'^(?P<student_id>\d+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<student_id>\d+)/vote/$', views.vote, name='vote')
)
