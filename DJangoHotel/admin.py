from django.contrib import admin

# Register your models here.
from DJangoHotel.models import Hotel, Customer, RoomInfo,Order


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description')

class RoomInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','total', 'description')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','name','tel','cardid','roomtype','begin','end','totalprice','state')

class customerAdmin(admin.ModelAdmin):
    list_display = ('tel','name','cardid')

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Customer,customerAdmin)
admin.site.register(RoomInfo,RoomInfoAdmin)
admin.site.register(Order,OrderAdmin)