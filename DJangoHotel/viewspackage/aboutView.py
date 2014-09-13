# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response

# Create your views here.

from DJangoHotel.models import Hotel
def about(request):
    title='DJango Hotel'
    hotel=Hotel.objects.get(name='DJango Hotel')
    name=hotel.name
    description=hotel.description
    address=hotel.address


    return render_to_response('about.html',{'title':title,'name':name,'description':description,'address':address})