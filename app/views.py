from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,CreateView
from django.views.generic.detail import DetailView
from app.models import *

class home(TemplateView):
    template_name='app/home.html'

class school_list(ListView):
    model = School
    context_object_name = 'QSLSO'
    #queryset=School.objects.filter(scname='pyspiders')
    ordering = ['scname']
    template_name='school_list.html'
    
class school_detail(DetailView):
    model = School
    context_object_name = 'RSO'
    template_name='app/school_detail.html'
    
class school_create(CreateView):
    model = School
    fields = '__all__'
    template_name='app/school_form.html'