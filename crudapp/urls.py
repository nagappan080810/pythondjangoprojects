from django.conf.urls import include, url

from . import views

app_name = 'crudapp'
urlpatterns = [
    url('index', views.index, name='index'),
    url('inventory/additem', views.newitem, name='additem'),
    url(r'^inventory/(?P<item_id>[0-9]+)/edititem$', views.edititem, name='edititem'),
    url(r'^inventory/(?P<item_id>[0-9]+)/createitem/$', views.createitem, name='createitem'),
    url(r'^inventory/(?P<item_id>[0-9]+)/delete$', views.deleteitem, name='deleteitem'),
    url('inventory/(\d+)/', views.itemdetails, name='detail'),
    url('inventory', views.inventory, name='inventory'),
]