from django.conf.urls import url
from market import views
urlpatterns = [
    url(r'^mark/$',views.market),
    url(r'^market/(\d+)/(\d+)/(\d+)/',views.user_mark,name='marketing'),
    # 添加购物车
    url(r'^addshop/',views.addShop),
    url(r'^subshop/',views.subShop),
]