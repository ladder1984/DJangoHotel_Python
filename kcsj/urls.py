from django.conf.urls import include, url, patterns

from django.contrib import admin

from DJangoHotel.viewspackage.aboutView import about
from DJangoHotel.viewspackage.indexView import index
from DJangoHotel.viewspackage.orderResultView import orderResult
from DJangoHotel.viewspackage.orderView import order
from DJangoHotel.viewspackage.roomInfoView import roomInfo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'kcsj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', about),
    url(r'^roominfo/', roomInfo),
    url(r'^$', index),
    url(r'^order/',order),
    url(r'^orderresult/',orderResult)
]


