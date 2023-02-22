from django.urls import path
from frontend import views

urlpatterns =[
    path('welpage/',views.welpage,name="welpage"),
    path('abtpage/',views.abtpage,name="abtpage"),
    path('cntpage/',views.cntpage,name="cntpage"),
    path('prodis/<itemcatg>',views.prodis,name="prodis"),
    path('singpro/<int:dataid>/',views.singpro,name="singpro"),
    path('logpage/',views.logpage,name="logpage"),
    path('saveregister/', views.saveregister, name="saveregister"),
    path('customerloginpage/', views.customerloginpage, name="customerloginpage"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('contct/', views.contct, name="contct"),
]