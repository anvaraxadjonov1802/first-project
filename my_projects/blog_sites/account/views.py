from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        ex_user = CustomUser.objects.filter(email = email).first()
        if ex_user:
            return HttpResponse("<h1>Bu emailli akkaunt bor</h1>")
        elif password1 != password2:
            return HttpResponse("<h1>parol mos emas</h1>")
        else:
            user = CustomUser.objects.create_user(
                email = email,
                first_name =first_name,
                last_name = last_name,
                password = make_password(password1)
            )
            login(request=request, user=user)
            return redirect('maqola')
    return render(
        request=request,
        template_name='auth/register.html'
    )

def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email, password)
        # print(request.POST)
        user = authenticate(request=request, email=email, password = password)
        # print(check_password())
        if user:
            
            login(request=request, user=user)
            return redirect('log_in')
        else:
            return HttpResponse('<h1>Ma\'lumot xato kiritildi</h1>')

    return render(
        request=request,
        template_name='auth/login.html'
    ) 


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('maqola')