from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import sqlite3
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def homepage(request):
    return render(request, 'home/homepage.html')


def login(request):
    return render(request, 'home/login.html')


def collegemap(request):
    return render(request, 'home/collegemap.html')


def attendence(request):
    return render(request, 'home/attendence.html')


def marks(request):
    return render(request, 'home/marks.html')


def registration(request):
    return render(request, 'home/registration.html')

@csrf_exempt
def registrationcont(request):
    f2 = forms.RegistrationForm()
    if(request.method=="POST"):
        f2 = forms.RegistrationForm(request.POST)
        if(f2.is_valid()):
            f3 = f2.cleaned_data
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.connect()
            cur.execute('select status from student_entry where passcode=?',(f3['passcode']))
            result =cur.fetchone()
            if(result is None):
                f3['NonExistent.visible']=True
                return render(request,'home/registration.html',{'form ':f3})
            else:
                result2=''.join(result)
                if(result2=='P'):
                    return render(request, 'home/registration2.html')
                else:
                    f3['AlreadyDone.visible']=True
                return render(request,'home/registration.html',{'form ':f3})