from django.contrib.auth.models import User
from django import forms

class Profile():
    class Meta:
        model = User
        field = [ 'category' ]