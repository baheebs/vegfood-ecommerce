from django.urls import path
from apps import views
from django.urls import path
from apps import views
urlpatterns =[
    path('ind/',views.ind,name="ind"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('savedata/',views.savedata, name="savedata"),
    path('displaypage/',views.displaypage, name="displaypage"),
    path('editadminpage/<int:dataid>/',views.editadminpage, name="editadminpage"),
    path('updatedata/<int:dataid>/',views.updatedata, name="updatedata"),
    path('deletedata/<int:dataid>/', views.deletedata, name="deletedata"),
    path('addcatpage/',views.addcatpage,name="addcatpage"),
    path('savecat/', views.savecat, name="savecat"),
    path('discatpage/', views.discatpage, name="discatpage"),
    path('editcatpage/<int:dataid>/', views.editcatpage, name="editcatpage"),
    path('updatecatdata/<int:dataid>/', views.updatecatdata, name="updatecatdata"),
    path('deletecatdata/<int:dataid>/', views.deletecatdata, name="deletecatdata"),
    path('addpropage/',views.addpropage,name="addpropage"),
    path('savepro/', views.savepro, name="savepro"),
    path('dispropage/', views.dispropage, name="dispropage"),
    path('editpropage/<int:dataid>/', views.editpropage, name="editpropage"),
    path('updateprodata/<int:dataid>/', views.updateprodata, name="updateprodata"),
    path('deleteprodata/<int:dataid>/', views.deleteprodata, name="deleteprodata"),
    path('loginpage/',views.loginpage, name="loginpage"),
    path('adminlogin/',views.adminlogin, name="adminlogin"),
    path('adminlogout/',views.adminlogout, name="adminlogout"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecntdata/<int:dataid>/', views.deletecntdata, name="deletecntdata"),


]