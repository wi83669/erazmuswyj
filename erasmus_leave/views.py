# Create your views here.
from django.http import HttpResponse
import datetime
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from erasmus_leave.models import Osoba
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from erasmus_leave.models import *
from erasmus_leave.forms import ContactForm
from django.views.generic import ListView

'''
def index(request):
    latest_osoba_list = Osoba.objects.order_by('-imie')[:5]
    context = {'latest_osoba_list' : latest_osoba_list}
    return render(request, 'erasmus_leave/index.html',context)

def detail(request, osoba_id):
    osoba = get_object_or_404(Osoba, pk=osoba_id)
    return render(request, 'erasmus_leave/detail.html', {'osoba':osoba})

def results(request, osoba_id):
    osoba = get_object_or_404(Osoba, pk=osoba_id)
    return render(request, 'erasmus_leave/results.html', {'osoba':osoba})

'''    
class IndexView(generic.ListView):
    template_name='erasmus_leave/index.html' #potrzebne do okreslenia niestandardowej lokalizacji
    context_object_name = 'latest_osoba_list'
    
    def get_queryset(self):
        '''Return the last five published osobas.'''
        return Osoba.objects.order_by('-imie')[:5]
    
class OsobaList(ListView):
    model = Osoba

class DetailView(generic.DetailView):
    model = Osoba
    template_name='erasmus_leave/detail.html' 

class ResultsView(generic.DetailView):
    model = Osoba
    temlate_name = 'erasmus_leave/results.html'
    
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def updateosoba(request, osoba_id):
    o = get_object_or_404(Osoba, pk=osoba_id)
    try:
        imie = request.POST['imie']
    except (KeyError, Osoba.DoesNotExitst):
        return render(request, 'erasmus_leave/detail.html',{'osoba':o,'error_message':"Nie wypelniles pola imie."})
    else:
        o.imie = imie
        o.save()
        return HttpResponseRedirect(reverse('erasmus_leave:results', args=(o.id,)))

def osobaform(request):
    if request.method == 'POST': #If the form has been submitted...
        form = OsobaForm(request.POST)#, instance = osoba)
        if form.is_valid():
            osoba = form.save()
            return HttpResponseRedirect('/erasmus_leave/')
    else:
        form = OsobaForm()
    return render(request, 'erasmus_leave/osobaform.html',{
        'form': form,
    })
    
def osoba_editform(request, osoba_id):
    osoba = Osoba.objects.get(pk= osoba_id )
    if request.method == 'POST': #If the form has been submitted...
        form = OsobaForm(request.POST, instance = osoba) #, instance=osoba)
        if form.is_valid():
            osoba = form.save()
            return HttpResponseRedirect('/erasmus_leave/')
    else:
        form = OsobaForm(instance = osoba)
    return render(request, 'erasmus_leave/osobaform.html',{
        'form': form,
    })

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
        
            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)
        
            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'erasmus_leave/contact.html', {
        'form': form,
    })
