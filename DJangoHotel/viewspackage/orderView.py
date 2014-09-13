# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

# Create your views here.

from DJangoHotel.models import Order
def order(request):




    return render_to_response('order.html')