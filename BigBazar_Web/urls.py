from django.urls import path
from BigBazar_Web import views
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('aboutuspage/',views.aboutuspage,name='aboutuspage'),
    path('contactpage/',views.contactpage,name='contactpage'),
    path('productpage/',views.productpage,name='productpage'),
    path('discategorypage/<itemCatg>/',views.discategorypage,name='discategorypage'),
    path('singleproductpage/<int:dataid>/',views.singleproductpage,name='singleproductpage'),
    path('customerdetailspage/',views.customerdetailspage,name='customerdetailspage'),
    path('savecustomerdetails/',views.savecustomerdetails,name='savecustomerdetails'),
    path('customerloginpage/',views.customerloginpage,name='customerloginpage'),
    path('savecustomerlogin/',views.savecustomerlogin,name='savecustomerlogin'),
    path('logout/',views.logout,name='logout'),
    path('savecontact/',views.savecontact,name='savecontact')


    ]