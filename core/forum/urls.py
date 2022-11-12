from django.conf.urls import url
from forum.views import IndexView, board_topics, new_topic, topic_posts, reply_topic

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^boards/(?P<pk>\d+)/$', board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', new_topic, name='new_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', topic_posts, name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', reply_topic, name='reply_topic'),
]

