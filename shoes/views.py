from django.shortcuts import render

# Create your views here.
from shoes.forms import AddShoe, AddBrand
from shoes.models import Shoe, Brand


def index(request):
    list = Shoe.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'shoe/index.html', {'list': list, 'links': links})


def brand_index(request):
    list = Brand.objects.all()
    links = []
    for b in list:
        links.append(str(b.id) + '/change')

    return render(request, 'shoe/brand_index.html', {'list': list, 'links': links})


def change(request, id=None):
    o = Shoe.objects.get(id=id)
    if request.method == 'POST':
        form = AddShoe(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()

    form = AddShoe(instance=o)
    return render(request, 'base_form.html', {'form': form})


def brand_change(request, id=None):
    o = Brand.objects.get(id=id)
    if request.method == 'POST':
        form = AddBrand(request.POST, instance=o)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()

    form = AddBrand(instance=o)
    return render(request, 'base_form.html', {'form': form})


def add(request):
    if request.method == 'POST':
        form = AddShoe(request.POST)
        if form.is_valid():
            form.save()

    form = AddShoe()
    return render(request, 'base_form.html', {'form': form})



def add_brand(request):
    if request.method == 'POST':
        form = AddBrand(request.POST)
        if form.is_valid():
            form.save()

    form = AddBrand()
    return render(request, 'base_form.html', {'form': form})

