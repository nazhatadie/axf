from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import check_password, make_password

from index.models import userMdel


# Create your views here.

def regist(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        img = request.FILES.get('icon')
        password = make_password(password)
        try:
            registjudge = userMdel.objects.filter(username=username).get()
            return render(request, 'user/user_register.html', {'name': '用户已存在'})
        except:
            userMdel.objects.create(
                username=username,
                password=password,
                email=email,
                icon=img,

            )
            return render(request, 'user/user_login.html')

