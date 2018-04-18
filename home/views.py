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
    main_rank = request.POST.get('mains_rank', '')
    advance_rank = request.POST.get('advanced_rank', '')
    k = get_object_or_404(Profile, pk=request.session["user_id"])
    k.mains_rank = main_rank
    k.advanced_rank = advance_rank
    k.save()
    try:
        user = User.objects.get(pk=request.session["user_id"])
    except User.DoesNotExist:
        raise Http404("There is no college that matches with you")
    return render(request, 'predictor.html', {'user': user, 'college': college, 'department': department} )


def signup(request):
    name = request.POST.get('name', '')
    email = request.POST.get('mail', '')
    password = request.POST.get('password', '')
    # k = get_object_or_404(User, '')
    k = User.objects.create(name=name, mail=email, password=password)
    # k.save()
    return render(request, 'signup.html' , {})


def search(request):
    template = loader.get_template('search.html')
    college = request.POST.get('clg', '')
    k = get_object_or_404(College, c_name=college)
    locality = k.c_locality
    state = k.c_state
    country = k.c_country
    pincode = k.c_pincode
    link = k.c_link
    if pincode > 0:
        return HttpResponse(template.render(
            {'college': college, 'locality': locality, 'state': state, 'country': country, 'pincode': pincode,
             'link': link}, request))
    else:
        return HttpResponse("<h2> Invalid College </h2>")




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

	
	
