from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import loader
from .models import *

def index(request):
    return render(request, 'index1.html' , {})

def user(request):
    return render(request, 'user.html' , {})

def profile(request):
    return render(request, 'profile.html' , {})

def signin(request):
    return render(request, 'login.html' , {})


def display(request):
    all_colleges = College.objects.all()
    all_departments = Department.objects.all()
    all_users = User.objects.all()
    context = {
        'all_colleges': all_colleges,
        'all_departments': all_departments,
        'all_users': all_users
    }
    return render(request, 'display.html', context)


def details(request, college_id):
    try:
        college = College.objects.get(pk=college_id)
    except College.DoesNotExist:
        raise Http404("There is no such college")
    return render(request, 'result.html', {'college': college})


def users(request):
    all_colleges = College.objects.all()
    all_departments = Department.objects.all()
    all_users = User.objects.all()
    context = {
        'all_colleges': all_colleges,
        'all_departments': all_departments,
        'all_users': all_users
    }
    return render(request, 'users.html', context)



def predictor(request):
    college = College.objects.all()
    department = Department.objects.all()
    try:
        user = User.objects.get(pk=request.session["user_id"])
    except User.DoesNotExist:
        raise Http404("There is no college that matches with you")
    return render(request, 'predictor.html', {'user': user, 'college': college, 'department': department} )


def detail4(request):
    template=loader.get_template('user.html')
    context={
	
	}
    return HttpResponse(template.render(context,request))


def check(request):
    email = request.POST.get('mail', '')
    password = request.POST.get('passwd', '')
    k = get_object_or_404(User, mail=email)
    if k.password == password:
        request.session["user_id"] = k.pk
        return redirect('user')
    else:
        return redirect('signin')

	
	
