from django.contrib import admin
from django.urls import path
from . import views;
from . import views
from django.conf import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.login,name='login'),
    path('index',views.index,name='index'),
    path('postLogin',views.postLogin,name='postLogin'),
    path('register',views.register,name='register'),
    path('postRegister',views.postRegister,name='postRegister'),
    path('scanner',views.scanner,name='scanner'),
    path('addQrCode',views.addQrCode,name='addQrCode')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)