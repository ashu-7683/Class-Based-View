from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

from django.views.generic import TemplateView
from app.forms import *

#create views here
#returning string using FBV

def FBV(request):
    return HttpResponse("This is a Function Based View returning a string response.")
#returning string by using CBV 
class CBV(View): 
    def get(self,request): 
        return HttpResponse('This is CBV') 
    
#returning A HTML page by using FBV 

def FBV_page(request): 
    return render(request,'FBV_page.html') 

#returning A HTML page by using CBV 
class CBV_page(View): 
    def get(self,request): 
        return render(request,'CBV_page.html') 
    
# validating Form by using FBV 
def InsertByFbv(request): 
    ESMFO=StudentMF() 
    d={'ESMFO':ESMFO}
    if request.method=="POST": 
        SMFDO=StudentMF(request.POST) 
        if SMFDO.is_valid(): 
            SMFDO.save() 
            return HttpResponse("Data Saved Successfully")
    return render(request,'insert_by_fbv.html',d) 

# Validating Form By using CBV 
class InsertByCbv(View): 
    def get(self,request): 
        ESMFO=StudentMF() 
        d={'ESMFO':ESMFO}
        return render(request,'insert_by_fbv.html',d) 
    
    def post(self,request): 
        SMFDO=StudentMF(request.POST) 
        if SMFDO.is_valid(): 
            SMFDO.save() 
            return HttpResponse("Data Saved Successfully")

        
# # Dont use View Class whenever u r dealing with Templates and Forms