from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('item1', views.item1, name='item1'),
    path('item2', views.item2, name='item2'),
    path('item3', views.item3, name='item3'),
    path('item4', views.item4, name='item4'),
    path('item5', views.item5, name='item5'),
    path('item6', views.item6, name='item6'),
    path('item7', views.item7, name='item7'),
    path('item8', views.item8, name='item8'),
    path('item9', views.item9, name='item9'),
    path('item10', views.item10, name='item10'),
    path('item11', views.item11, name='item11'),
    path('item12', views.item12, name='item12'),
    path('item13', views.item13, name='item13'),
    path('item14', views.item14, name='item14'),
    path('item15', views.item15, name='item15')
]
