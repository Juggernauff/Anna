from django.shortcuts import render
from django.http import HttpResponse 


def index(request):
    return render(request, 'index.html')
    
def index2(request):
    return render(request, 'index2.html')

def about(request, name):
    return HttpResponse(f"About\n{name}")