from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^(\d+)/$',views.detail),
    url(r'^grades/$',views.grades),
    url(r'^grades/(\d+)$',views.gradesstudets),
    url(r'^blog/$',views.Blog),
    url(r'^blogco/$',views.Blogcon)
]