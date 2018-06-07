# -*- coding:utf-8 -*-

from django.db import models


# Create your models here.

class Main(models.Model):
    img = models.CharField(max_length=200)  # 图片
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=16)

    class Meta:
        abstract = True


class Slider(Main):
    class Meta:
        db_table = 'index_slider'


class Nav(Main):
    class Meta:
        db_table = 'index_nav'


class MustBuy(Main):
    class Meta:
        db_table = 'index_buy'


class Shop(Main):
    class Meta:
        db_table = 'shop'


class Show(Main):
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=100)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=1)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField(default=0)
    marketprice2 = models.FloatField(default=1)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField(default=0)
    marketprice3 = models.FloatField(default=1)

    class Meta:
        db_table = 'index_show'


# 闪购
class FoodType(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'foodtypes'


# 闪购展示
class Goods(models.Model):
    productid = models.CharField(max_length=16)  # 商品id
    productimg = models.CharField(max_length=200)  # 商品图片
    productname = models.CharField(max_length=100)  # 商品名称
    productlongname = models.CharField(max_length=200)  # 商品规格
    isxf = models.IntegerField(default=1)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=100)  # 规格
    price = models.FloatField(default=0)  # 折后价格
    marketprice = models.FloatField(default=1)  # 原价
    categoryid = models.CharField(max_length=16)  # 分类 id
    childcid = models.CharField(max_length=16)  # 子分类id
    childcidname = models.CharField(max_length=100)  # 名称
    dealerid = models.CharField(max_length=16)  #
    storenums = models.IntegerField(default=1)  # 排序
    productnum = models.IntegerField(default=1)  # 销量


# 用户模型
class userMdel(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64, unique=True)
    sex = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icons')  # 头像的图片
    is_delete = models.BooleanField(default=False)
    ticket = models.CharField(max_length=255, default=True)

    class Meta:
        db_table = 'user'


class CartModel(models.Model):
    user = models.ForeignKey(userMdel)  # 关联用户
    goods = models.ForeignKey(Goods)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)

    class Meta:
        db_table = 'cart'


# 订单
class OrderModel(models.Model):
    user = models.ForeignKey(userMdel)  # 关联用户
    o_num = models.CharField(max_length=64)
    # 0表示下单，但是没付款
    o_status = models.IntegerField(default=0)  # 表示状态
    o_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'


class OrderGoodsMdel(models.Model):
    goods = models.ForeignKey(Goods)  # 关联商品
    order = models.ForeignKey(OrderModel)  # 关联的订单
    goods_num = models.IntegerField(default=1)  # 商品的个数

    class Meta:
        db_table = 'order_goods'


class Userticket(models.Model):
    user = models.ForeignKey(userMdel)
    ticket = models.CharField(max_length=255)
    deadline = models.DateTimeField(default=True)

    class Meta:
        db_table = 'ticket'
