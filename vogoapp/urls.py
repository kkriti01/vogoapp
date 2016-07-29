from django.conf.urls import url
from django.contrib import admin


from cakesapi import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vogoapi/$', views.home),
    url(r'^cake/$', views.save)
]
