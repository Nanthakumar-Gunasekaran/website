from django.conf.urls import url
from . import views


app_name = 'securityapp'

urlpatterns = [

    # home dashboard
    url(r'^home/$', views.IndexView.as_view, name='home'),

    url(r'^$', views.IndexView.as_view(), name='index'),

    # securityapp/<account_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='account_details'),

    # add new account
    url(r'^account/add/$', views.AccountCreate.as_view(), name='account_add'),

    # account/24/
    url(r'^account/(?P<pk>[0-9]+)/$', views.AccountUpdate.as_view(), name='account_update'),

    # account/24/delete
    url(r'^account/(?P<pk>[0-9]+)/delete/$', views.AccountDelete.as_view(), name='account_delete'),

    # register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # logout
    url(r'logout/$', views.logout_view, name='logout'),
]
