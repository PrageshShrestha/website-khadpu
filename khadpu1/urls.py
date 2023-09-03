from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('khadpu' ,views.frontpage , name = 'home' ),
    path('gallery' , views.gallery , name='gallery'),
    path('add_new' , views.add , name = 'add'),
    path('add_gallery' , views.add_gallery , name = 'add_gallery'),
    path('destinations' , views.destinations , name = 'destinations'),
    path('politics' , views.politics , name = 'politics'),
    path('add_politics' , views.add_politics , name = 'add_politics'),
    path('navbar' , views.navbar , name = 'navbar'),
    path('add_text' , views.add_text , name = 'add_text'),
    path('more_info' , views.more_info , name = 'more_info'),
    path('data_view' , views.data_view , name='data_view'),
    path('login' , views.login),
    path('timeline/', views.timeline, name='timeline'),
    path('customize' , views.customize , name = 'customize'),
    path('true_customize', views.true_customize , name='true_customize'),
    path('info/<str:model>/<str:id>' , views.change_info , name = "info"),

]
