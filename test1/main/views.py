from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def create(request):
    return render(request, 'form/create.html')