from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from index.models import CartModel, OrderModel, OrderGoodsMdel
from index.views import allgoods_sum


# Create your views here.

def all_select():
    is_select = True
    carts = CartModel.objects.all()
    for cart in carts:
        if not cart.is_select:
            is_select = False
    return is_select


def user_cart(request):
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            user_cart = CartModel.objects.filter(user_id=user.id)
            carts_goods = CartModel.objects.filter(is_select=True)
            sum = 0
            for cart_good in carts_goods:
                goods_price = float(cart_good.goods.price) * int(cart_good.c_num)
                sum += goods_price
            sum = float('%.2f' % sum)
            select = all_select()
            return render(request, 'cart/cart.html', {'user_carts': user_cart, 'goods_sum': sum, 'all_select': select})
        else:
            return HttpResponseRedirect('/log/login/')


def select_shop(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '成功',
        }
        cart_id = request.POST.get('cart_id')
        user = request.user
        if user and user.id:
            carts = CartModel.objects.filter(id=cart_id).first()
            if carts.is_select:
                carts.is_select = False
            else:
                carts.is_select = True

            carts.save()
            select = all_select()
            data['is_select'] = carts.is_select
            sum = allgoods_sum()
            sum = float('%.2f' % sum)
            data['sum'] = sum
            data['all_select'] = select


        return JsonResponse(data)


def select_all(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '成功'
        }
        is_select = request.POST.get('select')
        if is_select == '1':
            is_select = 0
        else:
            is_select = '1'
        user = request.user
        if user and user.id:
            carts = CartModel.objects.all()
            if is_select =='1':
                for cart in carts:
                    cart.is_select = True
                    cart.save()
            if is_select == 0:
                for cart in carts:
                    cart.is_select = False
                    cart.save()
            cart_id = []
            for cart in carts:
                cart_id.append(cart.id)
            sum = allgoods_sum()
            sum = float('%.2f' % sum)

        data['sum'] = sum
        data['select'] = is_select
        data['cart_id'] = cart_id

        return JsonResponse(data)


# 下单

def order(request):
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            # 查询is_select为True的购物车的数据
            carts_goods = CartModel.objects.filter(is_select=True)
            # 创建订单
            order = OrderModel.objects.create(user_id=user.id, o_status=0)

            # 创建订单详情
            for carts in carts_goods:
                OrderGoodsMdel.objects.create(
                    goods_num=carts.c_num,
                    goods_id=carts.goods_id,
                    order_id=order.id,
                )
            carts_goods.delete()

        return HttpResponseRedirect(reverse('cart:showordershop', args=(str(order.id),)))


def showOrderShop(request, order_id):
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            order = OrderModel.objects.filter(id=order_id).first()
            order_goods_all = order.ordergoodsmdel_set.all()

        data = {
            'order_id': order_id,
            'order_goods_all': order_goods_all,
            'goods_sum': sum,

        }
    return render(request, 'order/order_info.html', data)


# 付款方法
def pay_money(request, order_id):
    if request.method == 'GET':
        OrderModel.objects.filter(id=order_id).update(o_status=1)

    return HttpResponseRedirect('/mine/mygoods/')


# 点击待付款的方法
def wait_pay(request):
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            orders = OrderModel.objects.filter(user_id=user.id, o_status=0)
            all_ordergoods = []
            for order in orders:
                order_goods = order.ordergoodsmdel_set.all()
                for goods in order_goods:
                    all_ordergoods.append(goods)
            data = {
                'all_ordergoods': all_ordergoods
            }
        return render(request, 'order/order_list_wait_pay.html', data)


def payed(request):
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            orders = OrderModel.objects.filter(user_id=user.id, o_status=1)
            all_ordergoods = []
            for order in orders:
                order_goods = order.ordergoodsmdel_set.all()
                for goods in order_goods:
                    all_ordergoods.append(goods)
            data = {
                'all_ordergoods': all_ordergoods
            }
            return render(request, 'order/order_list_payed.html', data)
