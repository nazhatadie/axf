from django.conf.urls import url
from cart import views
urlpatterns =[
    url(r'^user_cart/',views.user_cart),
    url(r'^select_shop/',views.select_shop),
    url(r'^select_all/',views.select_all),
    # 下单
    url(r'^generateOrder/',views.order),
    # 下单后的详细页面
    url(r'^showOrderShop/(\d+)/',views.showOrderShop,name='showordershop'),
    # 付款
    url(r'^pay/(\d+)/',views.pay_money),
    # 待付款页面
    url(r'^waitpay/',views.wait_pay),
    # 已经付款页面
    url(r'^payed/',views.payed),

]