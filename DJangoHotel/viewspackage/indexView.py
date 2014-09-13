# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

# Create your views here.

from DJangoHotel.models import Hotel
def index(request):
    hotel=Hotel.objects.get(name='DJango Hotel')
    description=hotel.description



    return render_to_response('index.html',{'description':description})