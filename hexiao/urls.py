from django.urls import path, re_path
from hexiao import views

# 核销应用路由
urlpatterns = [
    re_path(r'^index$', views.index),
    re_path(r'^query$', views.query),
    re_path(r'^add$', views.add_code),
    re_path(r'^verify$', views.verify),
    re_path(r'^okCode$', views.okCode),
    re_path(r'^add_code$', views.add)
]
