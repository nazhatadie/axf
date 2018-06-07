from django.shortcuts import render
from index.models import userMdel, OrderModel


# Create your views here.


def mine(request):
    if request.method == 'GET':
        data = {}
        user = request.user
        if user and user.id:
            wait_pay, payed = 0, 0
            orders = user.ordermodel_set.all()
            for order in orders:
                if order.o_status == 0:
                    wait_pay += 1
                if order.o_status == 1:
                    payed += 1

            data['wait_pay'] = wait_pay
            data['payed'] = payed

        return render(request, 'mine/mine.html', data)
