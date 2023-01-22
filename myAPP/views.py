from django.shortcuts import render, redirect
from django.http import HttpResponse
from myAPP.models import studentbb,regdb,prodb,cndb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def index(request):
     return HttpResponse("hello")

def indexpage(request):
    return render(request,"index.html")

def studpage(req):
    return render(req,"addstudent.html")


def studsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        pa = request.POST.get('password')
        ge = request.POST.get('gender')
        img = request.FILES['image']
        ci = request.POST.get('city')
        ad = request.POST.get('address')
        obj = studentbb(Name=na,Email=em,Password=pa,gender=ge,Image=img,City=ci,Address=ad)
        obj.save()
        return redirect(studpage)

def nextpage (request):
    data = studentbb.objects.all()
    return render(request, "displaydata.html", {'data': data})

def editpage (req, dataid):
    data = studentbb.objects.get(id=dataid)
    print(data)
    return render(req,"editdata.html", {'data': data})

def updatedata(request,dataid):
    if request.method == "POST":
         na =request.POST.get('name')
         em = request.POST.get('email')
         pa = request.POST.get('password')
         ad = request.POST.get('address')
         try:
             img=request.FILES['image']
             fs  = FileSystemStorage()
             file = fs.save(img.name,img)
         except MultiValueDictKeyError:
             file =studentbb.objects.get(id=dataid).Image
         studentbb.objects.filter(id=dataid).update(Name=na,Email=em,Password=pa,Address=ad,Image=file)
         return  redirect(nextpage)

def deletedata(request,dataid):
    data = studentbb.objects.filter(id=dataid)
    data.delete()
    return redirect(nextpage)

def Categorypage(req):
    return render(req,"Addcategory.html")

def regsave(request):
    if request.method == "POST":
        ca = request.POST.get('Category_Name')
        img = request.FILES['image']
        de = request.POST.get('Description')
        obj = regdb(Category_Name=ca,Image=img,Description=de)
        obj.save()
        return redirect(Categorypage)

def Categorydisplay(req):
    data = regdb.objects.all()
    return render(req, "CategoryDisplay.html", {'data': data})


def editcategory (req, dataid):
    data = regdb.objects.get(id=dataid)
    print(data)
    return render(req,"editcategory.html", {'data': data})

def editsave(request,dataid):
    if request.method=="POST":
         ca = request.POST.get('Category_Name')
         de = request.POST.get('Description')
         try:
             img = request.FILES['image']
             fs = FileSystemStorage()
             file = fs.save(img.name,img)
         except MultiValueDictKeyError:
              file = regdb.objects.get(id=dataid).Image
         regdb.objects.filter(id=dataid).update(Category_Name=ca,Description=de,Image=file)
         return redirect(Categorydisplay)

def deletecategory(request,dataid):
    data = regdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Categorydisplay)

def Addproduct(request,):
    data = regdb.objects.all()
    return render(request,"Addproduct.html",{'data':data})

def prosave(request):
    if request.method == "POST":
        ca = request.POST.get('Category')
        pn = request.POST.get('Product_Name')
        pr = request.POST.get('Product_Price')
        Qu = request.POST.get('Quantity')
        De = request.POST.get('Description')
        img = request.FILES['image']
        obj=prodb(Category_Name=ca, Product_Name=pn, Product_Price=pr,Quantity =Qu,Description =De, Image=img)
        obj.save()
        return redirect(Addproduct)

def prodisplay(req):
    data = prodb.objects.all()
    return render(req, "prodisplay.html", {'data': data})

def editpro(req,dataid):
    data = prodb.objects.get(id=dataid)
    da = regdb.objects.all()
    return render(req, "editpro.html", {'data': data, "da":da})


def Updatepro(request, dataid):
        if request.method == "POST":
            ca = request.POST.get('Category')
            pn = request.POST.get('Product_Name')
            pr = request.POST.get('Product_Price')
            Qu = request.POST.get('Quantity')
            De = request.POST.get('Description')
            try:
                img = request.FILES['image']
                fs = FileSystemStorage()
                file = fs.save(img.name, img)
            except MultiValueDictKeyError:
                file = prodb.objects.get(id=dataid).Image
            prodb.objects.filter(id=dataid).update(Category_Name=ca, Product_Name=pn, Product_Price=pr, Quantity=Qu,
                                                   Description=De, Image=img)
            return redirect(prodisplay)

def deletepro(request,dataid):
    data = prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(prodisplay)

def loginpage(request):
    return render(request,"adminlogin.html")



def adminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
         user = authenticate(username=username_r,password=password_r)
         if user is not None:
              login(request, user)
              request.session['username']=username_r
              request.session['password']=password_r
              return redirect(indexpage)
    else:
         messages.warning(request,"sorry....invalid username or password")
    return render(request,'adminlogin.html')

def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)



def npage (request):
    data = cndb.objects.all()
    return render(request, "cnpage.html", {'data': data})
