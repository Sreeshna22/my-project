from django.shortcuts import render,redirect
from django.http import HttpResponse
from Webapp.models import customerdetails,pagedb
from django.contrib import messages


# Create your views here.
from myAPP.models import regdb,prodb,cndb
def mypage(request):
    data = regdb.objects.all()
    return render(request,"Webpage.html",{'data':data})


def Abpage(request):
   return render(request, "Aboutpage.html")

def propage(request):
    data = prodb.objects.all()
    return render(request,"pro.html",{'data':data})


def Discategory(request,itemcatg):
    print('===itemcatg===',itemcatg)
    catg=itemcatg.upper()

    products=prodb.objects.filter(Category_Name=itemcatg)
    context={
        'products':products,
        'catg':catg
    }
    return render(request,"cdisplay.html",context)


def prdpage(request,dataid):
    data = prodb.objects.get(id=dataid)
    da = regdb.objects.all()
    return render(request,"pdetails.html",{'dat':data,'da':da})

def loginpage(request):
    return render(request,"login.html")

def cdata(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        confirm_password = request.POST.get('Confirm_Password')
        if password==confirm_password:

            obj = customerdetails(Username=username,Email=email,Password=password,Confirm_Password=confirm_password)
            obj.save()
            return redirect(loginpage)
        else:
          return render(request,'login.html',{'msg':"sorry.....password not matched"})

def Customerlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('Username')
        password_r = request.POST.get('Password')
        if customerdetails.objects.filter(Username=username_r,Password=password_r).exists():
            data = customerdetails.objects.filter(Username=username_r,Password=password_r)
            request.session['Username'] = username_r
            request.session['Password'] = password_r
            return redirect(mypage)
        else:
          messages.warning(request,"sorry....invalid username or password")
    return render(request,'login.html')

def Customerlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(mypage)



def spage(request):
   return render(request,"spage.html")


def bpage(request):
   return render(request,"page2.html")

def register_save(request):
    if request.method == "POST":
       fn = request.POST.get('name')
       la = request.POST.get('la')
       pno = request.POST.get('phone')
       da = request.POST.get('Date')
       msg= request.POST.get('address')
       obj = pagedb(First_Name=fn, Last_Name=la, Phone=pno,Date=da,Message=msg)
       obj.save()
       return redirect(bpage)


def Cnpage(request):
   return render(request, "Contactpage.html")

def cnsave(request):
    if request.method == "POST":
       na = request.POST.get('name')
       em = request.POST.get('Email')
       sub = request.POST.get('subject')
       ms = request.POST.get('message')
       obj = cndb(Name=na,Email=em,Subject=sub, Message=ms)
       obj.save()
       return redirect(Cnpage)


def mycartpage(request):
   return render(request, "mycartpage.html")
