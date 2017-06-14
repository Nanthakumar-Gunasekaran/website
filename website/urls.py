from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_view
from securityapp.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^securityapp/', include('securityapp.urls')),
    url(r'^$', auth_view.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_view.logout, {'next_page': '/login'}),
]
