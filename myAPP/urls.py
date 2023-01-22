from django.urls import path
from myAPP import views

urlpatterns =[
    path('index/',views.index,name='index'),
    path('indexpage/', views.indexpage, name='indexpage'),
    path('studpage/',views.studpage, name="studpage"),
    path('studsave/',views.studsave, name="studsave"),
    path('nextpage/',views.nextpage, name="nextpage"),
    path('editpage/<int:dataid>/',views.editpage,name="editpage"),
    path('updatedata/<int:dataid>/',views.updatedata,name="updatedata"),
    path('deletedata/<int:dataid>/',views.deletedata,name="deletedata"),
    path('Categorypage/',views. Categorypage, name=" Categorypage"),
    path('regsave/',views.regsave, name="regsave"),
    path('Categorydisplay/', views.Categorydisplay, name="Categorydisplay"),
    path('editcategory/<int:dataid>/',views.editcategory, name="editcategory"),
    path('editsave/<int:dataid>/',views.editsave, name="editsave"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('Addproduct/', views.Addproduct, name="Addproduct"),
    path('prosave/', views.prosave, name="prosave"),
    path('prodisplay/', views.prodisplay, name="prodisplay"),
    path('editpro/<int:dataid>/', views.editpro, name="editpro"),
    path('Updatepro/<int:dataid>/', views.Updatepro, name="Updatepro"),
    path('deletepro/<int:dataid>/', views.deletepro, name="deletepro"),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('Adminlogout/',views.Adminlogout,name='Adminlogout'),
    path('npage/',views.npage, name="npage"),
]

