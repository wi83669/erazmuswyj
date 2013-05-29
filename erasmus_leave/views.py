# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from erasmus_leave.models import Osoba
from django.http import Http404

def index(request):
    latest_osoba_list = Osoba.objects.order_by('-imie')[:5]
    context = {'latest_osoba_list' : latest_osoba_list}
    return render(request, 'erasmus_leave/index.html',context)
'''
    latest_osoba_list = Osoba.objects.order_by('-imie')[:5]
    template = loader.get_template('erasmus_leave/index.html')
    context = Context({
                       'latest_osoba_list': latest_osoba_list,
    })
    return HttpResponse(template.render(context))
'''

def detail(request, osoba_id):
    osoba = get_object_or_404(Osoba, pk=osoba_id)
    return render(request, 'erasmus_leave/detail.html', {'osoba':osoba})
'''
    try:
        osoba = Osoba.objects.get(pk=osoba_id)
    except Osoba.DoesNotExist:
        raise Http404
    return render(request, 'erasmus_leave/detail.html',{'osoba':osoba})
'''

def result(request, student_id):
    return HttpResponse("You're looking at the result of student %s." % student_id)

def vote(request, student_id):
    return HttpResponse("You're voting on student %s." % student_id)