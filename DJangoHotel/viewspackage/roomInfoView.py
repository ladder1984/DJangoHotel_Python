# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response

# Create your views here.

from DJangoHotel.models import RoomInfo
def roomInfo(request):
    roomInfoList=RoomInfo.objects.all()
    return render_to_response('roominfo.html',{'roomInfoList':roomInfoList})
