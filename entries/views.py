from django.shortcuts import render

def index(request):
    template = 'entries/index.html'
    return render(request,template)

def add(request):
    template = 'entries/add.html'
    return render(request,template)
