from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def index(request):
    template = 'entries/index.html'
    entry_object_list = Entry.objects.order_by('-date_posted')
    context = {'entry_object_list':entry_object_list}
    return render(request,template,context)

def add(request):

    if request.method == 'POST':
        print(0)
        form = EntryForm(request.POST)
        print (1)

        if form.is_valid():
            print(2)
            form.save()
            print(3)
            return redirect('home')


    else:
        form = EntryForm()
        context = {'form':form}
        template = 'entries/add.html'
        return render(request,template,context)
