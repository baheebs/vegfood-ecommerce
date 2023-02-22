from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from apps.models import customer,category,proddetails,msgdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from frontend.views import contct
# Create your views here.

def ind(request):
    return render(request,"index.html")

def adminpage(req):
    return render(req,"addadmin.html")

def savedata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pas = request.POST.get('password')
        Con = request.POST.get('contactnumber')
        Em = request.POST.get('email')
        Us = request.POST.get('username')
        Img = request.FILES['image']
        obj = customer(Name=na, Contactnumber=Con, password=pas, Email=Em,username=Us,Image=Img)
        obj.save()
        return redirect(adminpage)

def displaypage(request):
    data = customer.objects.all()
    return render(request,"display.html",{'data':data})

def editadminpage(request,dataid):
    data = customer.objects.get(id=dataid)
    print(data)
    return render(request,"editadmin.html",{'data':data})

def updatedata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        pas = request.POST.get('password')
        Con = request.POST.get('contactnumber')
        Em = request.POST.get('email')
        Us = request.POST.get('username')
        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = customer.objects.get(id=dataid).Image
        customer.objects.filter(id=dataid).update(Name=na, Contactnumber=Con, password=pas, Email=Em,username=Us,Image=file)
        return redirect(displaypage)

def deletedata(req,dataid):
    data = customer.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypage)

def addcatpage(req):
    return render(req,"addcat.html")

def savecat(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        Img = request.FILES['image']
        obj = category(Name=na,Desc=de, Image=Img)
        obj.save()
        return redirect(addcatpage)

def discatpage(request):
    data = category.objects.all()
    return render(request,"discat.html",{'data':data})

def editcatpage(request,dataid):
    data = category.objects.get(id=dataid)
    print(data)
    return render(request,"editcat.html",{'data':data})

def updatecatdata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = category.objects.get(id=dataid).Image
        category.objects.filter(id=dataid).update(Name=na,Desc=de,Image=file)
        return redirect(discatpage)

def deletecatdata(req,dataid):
    data = category.objects.filter(id=dataid)
    data.delete()
    return redirect(discatpage)

def addpropage(req):
    data = category.objects.all()
    return render(req,"addpro.html",{'data':data})

def savepro(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        ca = request.POST.get('category')
        Img = request.FILES['image']
        obj = proddetails(Name=na,Desc=de,price=pr,Quantity=qu,category=ca,Image=Img)
        obj.save()
        return redirect(addpropage)

def dispropage(request):
    data = proddetails.objects.all()
    return render(request,"dispro.html",{'data':data})

def editpropage(request,dataid):
    data = proddetails.objects.get(id=dataid)
    da = category.objects.all()
    print(data)
    return render(request,"editpro.html",{'data':data, 'da':da})

def updateprodata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        ca = request.POST.get('category')

        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = proddetails.objects.get(id=dataid).Image
        proddetails.objects.filter(id=dataid).update(Name=na,Desc=de,price=pr,Quantity=qu,category=ca,Image=file)
        # data = category.objects.all()
        return redirect(dispropage)

def deleteprodata(req,dataid):
    data = proddetails.objects.filter(id=dataid)
    data.delete()
    return redirect(dispropage)

def loginpage(request):
    return render(request,"login.html")

def adminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request,user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(ind)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def displaycontact(request):
    data = msgdb.objects.all()
    return render(request,"dismsg.html",{'data':data})

def deletecntdata(req,dataid):
    data = msgdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)