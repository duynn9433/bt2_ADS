from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from about.forms import RegisteForm


def index(request):
    return render(request, 'about/home.html')


def contact(request):
    return render(request, 'about/contact.html')


def regiter(request):
    form = RegisteForm()
    if request.method == 'POST':
        form = RegisteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'about/register.html', {'form': form})

