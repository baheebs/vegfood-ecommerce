from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.models import category,proddetails,msgdb
from frontend.models import registerdb
from django.contrib import messages

# Create your views here.
def welpage(request):
    data = category.objects.all()
    # da = proddetails.objects.all()
    return render(request,"welcome.html",{'data' : data})

def abtpage(request):
    data = category.objects.all()
    return render(request,"aboutus.html",{'data' : data})

def cntpage(request):
    return render(request,"contact.html")
def prodis(request,itemcatg):
    print("===itemcatg===",itemcatg)
    catg = itemcatg.upper()
    products=proddetails.objects.filter(category  =itemcatg)
    context={
        'products':products,
        'catg':catg
    }
    return render(request,"productdisplay.html",context)

def singpro(request,dataid):
    data = proddetails.objects.get(id=dataid)
    return render(request,"singleprod.html",{'dat':data})

def logpage(request):
    return render(request,"loginout.html")

def saveregister(request):
    if request.method == "POST":
        na = request.POST.get('nam1')
        Em = request.POST.get('mail1')
        pas = request.POST.get('pass1')
        Con = request.POST.get('conpass')
        obj = registerdb(name=na, conpassword=Con, password=pas, mail=Em)
        obj.save()
        messages.success(request,"register successfully")
        return redirect(logpage)

def customerloginpage(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if registerdb.objects.filter(name=username_r,password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r
            messages.success(request,"login successfully")
            return  redirect(welpage)

        else:
            messages.error(request,"invalid user")
    return render(request,'loginout.html')

def userlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"logout successfully")
    return redirect(welpage)

def contct(request):
    if request.method == "POST":
        na = request.POST.get('nam2')
        Em = request.POST.get('mail2')
        su = request.POST.get('subj')
        Ms = request.POST.get('message')
        obj = msgdb(name=na, messge=Ms, sub=su, mail=Em)
        obj.save()
        return redirect(cntpage)
