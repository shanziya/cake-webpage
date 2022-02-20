from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.http import JsonResponse
from .models import Place, District

def cakeprodct(request):
    return render(request,"category.html")

def register(request):
    if request.method == "POST":
        customer_name = request.POST['username']
        customer_email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(customer_name,customer_email,password)
        myuser.save()

        messages.success(request,"your account has been successfully created")
        return redirect('cake_shop:login')

    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('cake_shop:cake_order_page')
    else:
        form = AuthenticationForm()
    context = {}
    context['form'] = form
    return render(request,'login.html',context)


def cake_order_page(request):
    context = {}
    context['district_list'] = District.objects.all()

    district = request.GET.get('district', None)
    if request.method == 'GET' and district:
        if district is not None:
            _places = []
            places = Place.objects.filter(district__name__iexact=district).values_list('name', flat=True)
            for place in places:
                _places.append(place)
            return JsonResponse({'places': _places})

    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            form.save()

            return redirect('cake_shop:cake_list_page')
    else:
        form = AuthenticationForm()
        context['form'] = form
    return render(request,'cake_order_page.html',context)

def cake_list_page(request):
    return render(request, 'cake_list_page.html')




