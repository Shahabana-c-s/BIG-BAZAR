from django.urls import path
from BigBazar_App import views

urlpatterns=[
    path('indexpage/',views.indexpage,name='indexpage'),
    path('addadminpage/',views.addadminpage,name='addadminpage'),
    path('saveadmindata/',views.saveadmindata,name='saveadmindata'),
    path('displayadminpage/',views.displayadminpage,name='displayadminpage'),
    path('editadminpage/<int:dataid>/', views.editadminpage, name='editadminpage'),
    path('updateadminpage/<int:dataid>/', views.updateadminpage, name='updateadminpage'),
    path('deleteadminpage/<int:dataid>/', views.deleteadminpage, name='deleteadminpage'),
    path('addcategorypage/',views.addcategorypage,name='addcategorypage'),
    path('savecategorydata/',views.savecategorydata,name='savecategorydata'),
    path('displaycategorypage/',views.displaycategorypage,name='displaycategorypage'),
    path('editcategorypage/<int:dataid>/',views.editcategorypage,name='editcategorypage'),
    path('updatecategorypage/<int:dataid>/',views.updatecategorypage,name='updatecategorypage'),
    path('deletecategorypage/<int:dataid>/',views.deletecategorypage,name='deletecategorypage'),
    path('addproductpage/',views.addproductpage,name='addproductpage'),
    path('saveproductdata/',views.saveproductdata,name='saveproductdata'),
    path('displayproductpage/',views.displayproductpage,name='displayproductpage'),
    path('editproductpage/<int:dataid>/',views.editproductpage,name='editproductpage'),
    path('updateproductpage/<int:dataid>/',views.updateproductpage,name='updateproductpage'),
    path('deleteproductpage/<int:dataid>/',views.deleteproductpage,name='deleteproductpage'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('savelogindata/',views.savelogindata,name='savelogindata'),
    path('logoutpage/',views.logoutpage,name='logoutpage'),
    path('displaymessage/', views.displaymessage, name='displaymessage'),

    ]