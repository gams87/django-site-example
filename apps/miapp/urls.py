from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index_view'),
    url(r'^contact/$', views.contact_view, name='contact_view'),
    url(r'^products/$', views.products_view, name='products_view'),
]