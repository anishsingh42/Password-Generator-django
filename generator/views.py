from django.shortcuts import render
from django.http import HttpResponse

import string
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length'))
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    punctuation = string.punctuation

    characters = []

    if request.GET.get('uppercase'):
        characters.extend(list(uppercase))
    if request.GET.get('lowercase'):
        characters.extend(list(lowercase))
    if(request.GET.get('numbers')):
        characters.extend(list(numbers))
    if(request.GET.get('punctuation')):
        characters.extend(list(punctuation))
    
    password = ''
    for x in range(length):
        password += random.choice(characters)
    return render(request, 'generator/home.html', {'password': password})
