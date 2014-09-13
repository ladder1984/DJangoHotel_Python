# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from DJangoHotel.models import Order,RoomInfo,Customer
import time
import datetime
def orderResult(request):

    tempCustomer=Customer()
    tempCustomer.tel= request.GET['tel']
    tempCustomer.name= request.GET['name']
    tempCustomer.cardid= request.GET['cardid']
    tempCustomer.save()

    tempOrder=Order()
    tempOrder.name = request.GET['name']
    tempOrder.tel = request.GET['tel']
    tempOrder.cardid = request.GET['cardid']
    tempOrder.roomtype = request.GET['roomtype']

    begin = request.GET['begin']
    end = request.GET['end']
    tempOrder.begin = (datetime.datetime.strptime(begin , '%Y-%m-%d')).date()
    tempOrder.end = (datetime.datetime.strptime(end , '%Y-%m-%d')).date()
    period = (tempOrder.end - tempOrder.begin).days

    price = 0

    if tempOrder.roomtype == 'standard':
        price = (RoomInfo.objects.get(name='标准间')).price

    elif tempOrder.roomtype =='better':
        price = (RoomInfo.objects.get(name='豪华间')).price

    elif tempOrder.roomtype =='president':
        price = (RoomInfo.objects.get(name='总统间')).price


    tempOrder.totalprice = period * price
    tempOrder.save()

    tel = request.GET['tel']
    begin = request.GET['begin']

    return render_to_response('orderresult.html',{'orderid':tempOrder.id})