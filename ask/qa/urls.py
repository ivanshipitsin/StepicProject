from django.conf.urls import url

urlpatterns =[
    url(r'^',qa.views.test,name='test'),
    url(r'^login/',qa.views.test,name='login'),
    url(r'^signup/',qa.views.test,name='signup'),
    url(r'^question/(?P<pk>\d+)/$',qa.views.test,name='question'),
    url(r'^ask/',qa.views.test,name='ask'),
    url(r'^popular/',qa.views.test,name='popular'),
    url(r'^new/',qa.views.test,name='new')
]
