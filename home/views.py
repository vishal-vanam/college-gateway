from django.shortcuts import render
from django.http import Http404
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



def predictor(request, user_id):
    college = College.objects.all()
    department = Department.objects.all()
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("There is no college that matches with you")
    return render(request, 'predictor.html', {'user': user, 'college': college, 'department': department} )

