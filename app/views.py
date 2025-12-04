import re
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from app.models import *
from django.urls import reverse_lazy

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
class school_update(UpdateView):
    model=School
    fields='__all__'
    
class school_delete(DeleteView):
    model=School
    context_object_name='DSO'
    success_url=reverse_lazy('school_list')