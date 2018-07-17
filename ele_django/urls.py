"""ele_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from ele_django import views

# 功能
from function import views as functionViews
# 用户
from user.views import signUp, signIn

urlpatterns = [
    path('admin/', admin.site.urls),
    # 测试
    url('^$', views.index, name='index'),
    # 注册
    url('^user/signup/$', signUp().as_view(), name='signUp'),
    # 登录
    url('^user/signin/$', signIn().as_view(), name='signIn'),
    # 图片验证码
    url('^user/imagecode/$', functionViews.imageCode, name='imageCode'),
]


