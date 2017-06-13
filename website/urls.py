from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^securityapp/', include('securityapp.urls')),
    url(r'^$', auth_view.login, name='login'),
    url(r'^logout/$', auth_view.logout, name='logout')
]
