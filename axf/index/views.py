from django.shortcuts import render
from index.models import Slider, Nav, MustBuy, Shop, Show, FoodType,CartModel


# Create your views here.

def home(request):
    datas = Slider.objects.all()
    navs_data = Nav.objects.all()
    must_buy = MustBuy.objects.all()
    shop = Shop.objects.all()
    shows = Show.objects.all()
    data={
        'datas':datas,
        'navs_data': navs_data,
        'must_buy': must_buy,
        'shops': shop,
        'shows': shows

    }
    return render(request, 'home/home.html', data)




def allgoods_sum():
    carts_goods = CartModel.objects.filter(is_select=True)
    sum = 0
    for cart_good in carts_goods:
        goods_price = float(cart_good.goods.price) * int(cart_good.c_num)
        sum += goods_price
    return sum
