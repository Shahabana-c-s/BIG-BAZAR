from django.shortcuts import render,redirect
from BigBazar_App.models import admindb,categorydb,productdb,contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def addadminpage(request):
    return render(request,"AddAdmin.html")
def saveadmindata(request):
    if request.method=="POST":
        na=request.POST.get('name')
        mn=request.POST.get('mobile')
        em=request.POST.get('email')
        im=request.FILES['image']
        un=request.POST.get('username')
        pw=request.POST.get('password')
        cp=request.POST.get('confirm')
        obj=admindb(Name=na,Mobile=mn,Email=em,Image=im,Username=un,Password=pw,Confirm=cp)
        obj.save()
        return redirect(addadminpage)
def displayadminpage(request):
    data=admindb.objects.all()
    return render(request,"DisplayAdmin.html",{'data':data})
def editadminpage(request,dataid):
    data=admindb.objects.get(id=dataid)
    print(data)
    return render(request,"EditAdmin.html",{'data':data})
def updateadminpage(request,dataid):
    if request.method == "POST":
        na=request.POST.get('name')
        mn=request.POST.get('mobile')
        em=request.POST.get('email')
        un=request.POST.get('username')
        pw=request.POST.get('password')
        cp=request.POST.get('confirm')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=na,Mobile=mn,Email=em,Image=file,Username=un,Password=pw,Confirm=cp)
        return redirect(displayadminpage)
def deleteadminpage(request,dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(addadminpage)


def addcategorypage(request):
    return render(request,"AddCategory.html")
def savecategorydata(request):
    if request.method == "POST":
        cn=request.POST.get('name')
        ds=request.POST.get('description')
        img=request.FILES['catimage']
        obj=categorydb(Name=cn,Description=ds,CategoryImage=img)
        obj.save()
        return redirect(addcategorypage)
def displaycategorypage(request):
    data=categorydb.objects.all()
    return render(request,"DisplayCategory.html",{'data':data})
def editcategorypage(request,dataid):
    data=categorydb.objects.get(id=dataid)
    print(data)
    return render(request,"EditCategory.html",{'data':data})
def updatecategorypage(request,dataid):
    if request.method == "POST":
        cn=request.POST.get('name')
        ds=request.POST.get('description')
        try:
            img=request.FILES['catimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).CategoryImage
        categorydb.objects.filter(id=dataid).update(Name=cn,Description=ds,CategoryImage=file)
        return redirect(displaycategorypage)
def deletecategorypage(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategorypage)

def addproductpage(request):
    data=categorydb.objects.all()
    return render(request,"AddProduct.html",{'data':data})
def saveproductdata(request):
    if request.method == "POST":
        pn=request.POST.get('pname')
        pr=request.POST.get('price')
        qt=request.POST.get('quantity')
        pd=request.POST.get('pdescription')
        pi=request.FILES['pimage']
        ct=request.POST.get('cat')
        obj=productdb(Product_Name=pn,Price=pr,Quantity=qt,Product_Description=pd,Product_Image=pi,Category=ct)
        obj.save()
        return redirect(addproductpage)
def displayproductpage(request):
    data=productdb.objects.all()
    return render(request,"DisplayProduct.html",{'data':data})
def editproductpage(request,dataid):
    data=productdb.objects.get(id=dataid)
    da=categorydb.objects.all()
    print(data)
    return render(request,"EditProduct.html",{'data':data,'da':da})
def updateproductpage(request,dataid):
    if request.method == "POST":
        pn=request.POST.get('pname')
        pr=request.POST.get('price')
        qt=request.POST.get('quantity')
        pd=request.POST.get('pdescription')
        ct=request.POST.get('cat')
        try:
            pi=request.FILES['pimage']
            fs=FileSystemStorage()
            file=fs.save(pi.name,pi)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).Product_Image
        productdb.objects.filter(id=dataid).update(Product_Name=pn,Price=pr,Quantity=qt,Product_Description=pd,Product_Image=file,Category=ct)
        return redirect(displayproductpage)
def deleteproductpage(request,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproductpage)
def loginpage(request):
    return render(request,"login.html")
def savelogindata(request):
    if request.method=="POST":
        Username_L=request.POST.get('username')
        Password_L=request.POST.get('password')
        if User.objects.filter(username__contains=Username_L).exists():
            user=authenticate(username=Username_L,password=Password_L)
            if user is not None:
                login(request,user)
                request.session['username']=Username_L
                request.session['password']=Password_L
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def logoutpage(request):
    del request.session['username']
    del request.session['password']
    return redirect (indexpage)
def displaymessage(request):
    data=contactdb.objects.all()
    return render(request,"Messages.html",{'data':data})




