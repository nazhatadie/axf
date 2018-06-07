from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.core.urlresolvers import reverse

from index.models import FoodType, Goods,CartModel

from index.views import allgoods_sum


# Create your views here.


def market(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('mark:marketing', args=('104749', '0', '0')))


def user_mark(request, typeid, cid, sort_id):
    if request.method == 'GET':
        data = {}
        # 全部食物分类
        foodtypes = FoodType.objects.all()
        # 食物分类的数据
        if cid == '0':
            goods_types = Goods.objects.filter(categoryid=typeid)
        else:
            goods_types = Goods.objects.filter(categoryid=typeid,childcid=cid)
        # 食物分类的子类
        foods_childnames = FoodType.objects.get(typeid=typeid)
        foods_classify = foods_childnames.childtypenames
        foods_list = foods_classify.split('#')
        foods_datas = []
        for foods in foods_list:
            foods_datas.append(foods.split(':'))

        # 排序
        if sort_id =='0':
            pass
        if sort_id =='1':
            goods_types = goods_types.order_by('productnum')
        if sort_id =='2':
            goods_types = goods_types.order_by('-price')
        if sort_id =='3':
            goods_types = goods_types.order_by('price')

        data['foodtypes'] = foodtypes
        data['typeid'] = typeid
        data['cid'] = cid
        data['goods_types'] = goods_types
        data['foods_subclass'] = foods_datas

        return render(request, 'market/market.html', data)

# 增加数据
def addShop(request):
    if request.method =='POST':
        data = {
            'code':200,
            'msg':'成功',
        }
        user = request.user
        if user and user.id:
            goods_id = request.POST.get('goods_id')
            user_carts = CartModel.objects.filter(user=user,goods_id=goods_id).first()
            if user_carts:
                user_carts.c_num += 1
                user_carts.save()
                data['c_num'] = user_carts.c_num
            else:
                CartModel.objects.create(
                    user=user,
                    goods_id=goods_id,
                    c_num=1,
                )
                data['c_num']=1
            sum = allgoods_sum()
            sum = float('%.2f'% sum)
            data['goods_id'] =goods_id
            data['sum'] = sum
        return JsonResponse(data)

# 删除数据
def subShop(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '成功',
        }
        user = request.user
        if user and user.id:
            goods_id = request.POST.get('goods_id')
            user_cart = CartModel.objects.filter(user=user,goods_id=goods_id).first()
            if user_cart:
                if user_cart.c_num == 1:
                    user_cart.delete()
                    data['c_num'] = 0
                else:
                    user_cart.c_num -= 1
                    user_cart.save()
                    data['c_num'] = user_cart.c_num
            sum = allgoods_sum()
            sum = float('%.2f' % sum)
            data['goods_id'] = goods_id
            data['sum'] = sum

            return JsonResponse(data)


