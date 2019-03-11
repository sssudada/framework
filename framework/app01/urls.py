# -*- coding: utf-8 -*-


from django.conf.urls import patterns


# 测试db_mfw表
urlpatterns = patterns(
    'app01.views',
    (r'^index/$', 'index'),
    (r'^create/$', 'create_tserver'),
    (r'^delete/(.+)/(.+)/(.+)/$', 'delete_tserver'),
    (r'^change/(.+)/(.+)/(.+)/(.+)/(\d+)/(\d+)/$', 'change_tserver'),
    (r'^select/$', 'select_tserver'),
)
