"""
URL configuration for mobile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from features.views import MobileView,MobileList,MobileDetail,Mobiledelete,Mobileupdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mob/',MobileView.as_view(),name="add"),
    path('mob_list/',MobileList.as_view(),name="det"),
    path('mob_detail/<int:pk>',MobileDetail.as_view(), name="mobile"),
    path('mob_list/<int:pk>/remove',Mobiledelete.as_view(),name="del"),
    path('mob/<int:pk>/edit',Mobileupdate.as_view(),name="edit")
]
