from django.urls import path

from div import views
urlpatterns =[
     path('',views.home,name='home'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     path('checkout/',views.checkout,name='checkout'),
     path('services/',views.services,name='services'),
     path('cart/',views.cart,name='cart'),
     path('blog/',views.blog,name='blog'),
     path('Shop/',views.shop,name='Shop      '),
     path('thankyou/',views.thankyou,name='thankyou'),

 ]
