from django.conf.urls import url
from . import views


app_name = 'securityapp'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),

    # accounts/<account_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='account_details'),

    # add new account
    url(r'^account/create/$', views.AccountCreate.as_view(), name='account_add'),

    # account/24/
    url(r'^account/(?P<pk>[0-9]+)/$', views.AccountUpdate.as_view(), name='account_update'),

    # album/24/delete
    url(r'^account/(?P<pk>[0-9]+)/delete/$', views.AccountDelete.as_view(), name='account_delete'),

    # logout
    url(r'logout/$', views.logout_view, name='logout'),
]
