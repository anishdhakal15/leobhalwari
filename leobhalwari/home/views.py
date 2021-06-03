from django.shortcuts import render,HttpResponse
from .models import Testimonial,Advisor,leader,Team,Service
import random
from math import ceil

# Create your views here.
def home(request):
    if request.method=='GET':
        testimonial = [i for i in Testimonial.objects.all()]
        advisor = [i for i in Advisor.objects.all()][:3]
        serv=[i for i in Service.objects.all()][:8]
        # serv=range(16)
        n=len(serv)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        return render(request,'index.html',{'testas':testimonial,'advisors':advisor,'product':reversed(serv),'range':range(1,nSlides)})

def history(request):
    if request.method=='GET':
        return render(request,'history.html')

def leaders(request):
    if request.method=='GET':
        leaders=leader.objects.all()
        return render(request,'leaders.html',{'leaders':leaders})
def team(request):
    if request.method=='GET':
        bod=Team.objects.all()
        return render(request,'teams.html',{'bods':bod})

def services(request):
    if request.method=='GET':
        sers=Service.objects.all()
        return render(request,'service.html',{'sers':reversed(sers)})

def donate(request):
    if request.method=='GET':
        return render(request,'donate.html')
