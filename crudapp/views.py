# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from .models import Inventory
from .forms import InventoryForm
import datetime

# Create your views here.
def index(request): 
    return HttpResponse("Hello World! You are into the CRUD app.")

def newitem(request): 
    item = Inventory()
    item.id = 0
    template = loader.get_template('inventory/itemstock.html')
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context, request))

def edititem(request, item_id): 
    item = Inventory.objects.get(id=item_id)
    print(item.id)
    template = loader.get_template('inventory/itemstock.html')
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context, request))

def deleteitem(request, item_id): 
    print(item_id)
    Inventory.objects.filter(id=item_id).delete()
    return HttpResponse("Deleted successfully")

def createitem(request, item_id): 
    params = request.POST
    print(item_id)
    print(item_id>0)
    if int(item_id) > 0: 
        item = Inventory.objects.get(id=item_id)        
    else: 
        print('else part')
        item = Inventory()
    item.item_id = params['itemId']
    item.item_name = params['itemName']
    item.item_available_qty = params['availableQty']
    item.brand_name = params['brandName']
    item.last_updated = datetime.datetime.now()
    item.save()
    print(item.id)
    return HttpResponse("saved successfully")

def inventory(request):
    inventory_list = Inventory.objects.all()
    template = loader.get_template('inventory/inventory.html')
    context = {
        'inventory_list': inventory_list,
    }
    print(inventory_list)
    return HttpResponse(template.render(context, request))

def itemdetails(request, item_id):
    item = Inventory.objects.filter(item_id=item_id)
    template = loader.get_template('inventory/itemstock.html')
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context, request))

