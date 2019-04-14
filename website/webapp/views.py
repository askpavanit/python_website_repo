from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return render(request,'index.html')

def python(request):
    return render(request,'python.html')
    # return redirect('https://www.w3schools.com/python/python_intro.asp')

def copyright(request):
    return render(request,'copyright.html')

def contact(request):
    return render(request,'contact.html')

def django(request):
    return render(request,'django.html')