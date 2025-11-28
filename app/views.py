from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.views.generic import TemplateView
from django.views.generic import FormView
from app.models import *
from django.http import HttpResponse


class RenderHtmlByTV(TemplateView):
    template_name = 'RenderHtmlByTV.html'

    def get_context_data(self, **kwargs):
        ECDO= super().get_context_data(**kwargs)
        ECDO['name'] = 'Ashu'
        ECDO['age'] = '23'
        return ECDO

class InsertByTV(TemplateView):
    template_name = 'InsertByTV.html'

    def get_context_data(self, **kwargs):
        ECDO= super().get_context_data(**kwargs)
        ECDO['ESMFO']=StudentMF()
        return ECDO

    def post(self, request):
        SMFDO=StudentMF(request.POST)
        if SMFDO.is_valid():
            SMFDO.save()
            return HttpResponse('Data Inserted Successfully')
        else:
            return HttpResponse('Data Insertion Failed')
        

class InsertByFV(FormView):
    template_name = 'InsertByFV.html'
    form_class = StudentMF
    
    def form_valid(self, form):
        form.save()
        return HttpResponse('Data Inserted Successfully using FormView')