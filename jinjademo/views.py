from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'jinjademo/index.html')


def detail(request):
    return render(request, 'jinjademo/detail.html')


def macro(request):
    return render(request, 'jinjademo/macro_call_list.html')
