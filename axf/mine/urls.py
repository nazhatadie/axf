from django.conf.urls import url
from mine import views
urlpatterns =[
    url(r'^mygoods/',views.mine)
]