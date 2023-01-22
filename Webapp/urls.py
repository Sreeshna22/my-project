from django.urls import path
from Webapp import views

urlpatterns =[
    path('mypage/',views.mypage,name='mypage'),
    path('Cnpage/',views.Cnpage,name='Cnpage'),
    path('Abpage/',views.Abpage,name='Abpage'),
    path('propage/',views.propage,name='propage'),
    path('Discategory/<itemcatg>',views.Discategory,name='Discategory'),
    path('prdpage/<int:dataid>/', views.prdpage, name='prdpage'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('cdata/',views.cdata,name='cdata'),
    path('Customerlogin/',views.Customerlogin,name='Customerlogin'),
    path('Customerlogout/', views.Customerlogout,name='Customerlogout'),
    path('bpage/', views.bpage, name='bpage'),
    path('spage/', views.spage, name='spage'),
    path('register_save/', views.register_save, name='register_save'),
    path('cnsave/', views.cnsave, name='cnsave'),
    path('mycartpage/', views.mycartpage, name='mycartpage'),
]