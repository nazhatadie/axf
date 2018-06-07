from datetime import datetime,timedelta
import random
import time
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
# Create your views here.
from index.models import userMdel,Userticket


def login(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if userMdel.objects.filter(username=username).exists():
            user = userMdel.objects.filter(username=username)
            if check_password(password,user[0].password):
                s = 'abcdefghijklmnopqrstuvwxyz1234567890'
                ticket = ''
                for i in range(15):
                    ticket += random.choice(s)

                now_time = int(time.time())
                out_time = datetime.now() + timedelta(days=1)
                ticket = 'TK_' + ticket + str(now_time)
                response = HttpResponseRedirect('/mine/mygoods/')
                response.set_cookie('ticket', ticket, expires=out_time)
                Userticket.objects.create(
                    user_id=user[0].id,
                    ticket=ticket,
                    deadline=out_time,
                )
                return response
            else:
                return render(request,'user/user_login.html',{'password':'密码错误'})

        else:
            return render(request,'user/user_login.html',{'password':'用户不存在'})


def logout(request):
    if request.method == 'GET':
        # 删除cookie
        response = HttpResponseRedirect('/index/index/')
        response.delete_cookie('ticket')
        ticket = request.COOKIES.get('ticket')
        Userticket.objects.filter(ticket=ticket).delete()
        return response