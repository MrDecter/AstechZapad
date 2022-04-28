from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('Proizvodstvennoe-zdanie-s-administrativno-bytovym-korpusom', views.item1, name='item1'),
    path('Skladskoe-zdanie', views.item2, name='item2'),
    path('Teplyj-sklad-dlya-hraneniya-avtozapchastej', views.item3, name='item3'),
    path('Skladskoj-logisticheskij-kompleks', views.item4, name='item4'),
    path('Magazin-roznichnoj-torgovli', views.item5, name='item5'),
    path('Holodnyj-sklad-dlya-hraneniya-materialov', views.item6, name='item6'),
    path('Stanciya-tekhnicheskogo-obsluzhivaniya-dlya-bolshegruznoj-tekhniki', views.item7, name='item7'),
    path('Cekh-po-vyrashchivaniyu-foreli', views.item8, name='item8'),
    path('Cekh-po-obsluzhivaniyu-legkovyh-avtomobilej-s-ABK', views.item9, name='item9'),
    path('Administrativno-bytovoj-korpus', views.item10, name='item10'),
    path('Holodnyj-sklad-dlya-hraneniya-stroitelnyh-materialov', views.item11, name='item11'),
    path('Torgovyj-kompleks', views.item12, name='item12'),
    path('Cekh-holodnoj-shtampovki', views.item13, name='item13'),
    path('Sklad-obshchego-naznacheniya', views.item14, name='item14'),
    path('Skladskoj-kompleks', views.item15, name='item15')
]
