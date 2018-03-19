from django.urls import path

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)