from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
# Create your views here.


def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')

    if u and p:

        c = PollsStudentinfo.objects.filter(stu_name=u, stu_psw=p).count()
        if c>=1:
            return HttpResponse("login success!")
        else:
            return HttpResponse("login password wrong!")
    else:
        return HttpResponse("please input correct user and pwd!")

#render the registration page
def toregister_view(request):
    return render(request, 'register.html')

#logical judgement after registration
def register_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')
    if u and p:
        stu = PollsStudentinfo(stu_id = str(random.randrange(1111,9999)), stu_name=u, stu_psw=p)
        stu.save()
        return HttpResponse("register success!")
    else:
        return HttpResponse("please input correct user and pwd!")
