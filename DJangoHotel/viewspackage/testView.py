# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response

# Create your views here.

from DJangoHotel.models import Hotel
def test(request):
    title='DJango Hotel'
    hotel=Hotel.objects.get(name='DJango Hotel')
    name=hotel.name
    description=hotel.description
    address=hotel.address


    return render_to_response('test.html',{'title':title,'name':name,'description':description,'address':address})