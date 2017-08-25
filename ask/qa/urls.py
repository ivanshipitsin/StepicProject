from django.conf.urls import url
from qa.views import test, news, popular, question, Ask
urlpatterns =[
    url(r'^$',news,name='test'),
    url(r'^login/',test,name='login'),
    url(r'^signup/',test,name='signup'),
    url(r'^question/(?P<pk>\d+)/$',question,name='question'),
    url(r'^ask/',Ask,name='ask'),
    url(r'^popular/',popular,name='popular'),
    url(r'^new/',test,name='new')
]
