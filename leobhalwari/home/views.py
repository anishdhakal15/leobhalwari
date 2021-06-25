from django.shortcuts import render,HttpResponse
from .models import Testimonial,Advisor,leader,Team,Service
import random
from math import ceil

def home(request):
    if request.method=='GET':
        testimonial = [i for i in Testimonial.objects.all()]
        advisor = [i for i in Advisor.objects.all()][:3]
        serv=[i for i in Service.objects.all()][:8]
        temp1=[]
        temp2 = []
        x=0
        for i in serv:
            if x<3:
                temp1.append(i)
                x+=1
            else:
                temp2.append(i)
        serv=[reversed(temp2),reversed(temp1)]
        # serv=range(16)
        n=len(serv)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        return render(request,'index.html',{'testas':testimonial,'advisors':advisor,'product':serv,'range':range(1,nSlides)})

def history(request):
    if request.method=='GET':
        return render(request,'history.html')

def leaders(request):
    if request.method=='GET':
        leaders=leader.objects.all()
        return render(request,'leaders.html',{'leaders':leaders})
def team(request):
    if request.method=='GET':
        bod=[i for i in Team.objects.all()]
        top = bod[:3]
        bod =bod[3:]
        return render(request,'teams.html',{'tops':top,'bods':bod})

def services(request):
    if request.method=='GET':
        sers=Service.objects.all()
        return render(request,'service.html',{'sers':reversed(sers)})

def donate(request):
    if request.method=='GET':
        return render(request,'donate.html')
