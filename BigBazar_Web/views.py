from django.shortcuts import render,redirect
from BigBazar_App.models import categorydb,productdb,contactdb
from BigBazar_Web.models import customerdetailsdb


# Create your views here.
def homepage(request):
    data=categorydb.objects.all()
    return render(request,"homepage.html",{'data':data})
def aboutuspage(request):
    data = categorydb.objects.all()
    return render(request,"aboutus.html",{'data':data})
def contactpage(request):
    data = categorydb.objects.all()
    return render(request,"contact.html",{'data':data})
def productpage(request):
    dat=productdb.objects.all()
    return render(request,"product.html",{'dat':dat})
def discategorypage(request,itemCatg):
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    data=categorydb.objects.all()
    products=productdb.objects.filter(Category=itemCatg)
    context = {
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,"DisCategory.html",context)
def singleproductpage(request,dataid):
    da=categorydb.objects.all()
    data=productdb.objects.get(id=dataid)
    return render(request,"SingleProduct.html",{'dat':data,'da':da})
def customerdetailspage(request):
    return render(request,"CustomerDetails.html")
def savecustomerdetails(request):
    if request.method == "POST":
        cn = request.POST.get('username')
        ce = request.POST.get('cemail')
        cp = request.POST.get('password')
        cc = request.POST.get('cconfirm')
        if cp == cc:
            obj=customerdetailsdb(username=cn,CEmail=ce,password=cp,CConfirm=cc)
            obj.save()
            return redirect(customerdetailspage)
        else:
            return render(request,"CustomerDetails.html",{'msg':"sorry..password not matched"})

def customerloginpage(request):
    return render(request,"CustomerLogin.html")
def savecustomerlogin(request):
    if request.method == "POST":
        username_c = request.POST.get('username')
        password_c = request.POST.get('password')
        if customerdetailsdb.objects.filter(username=username_c,password=password_c).exists():
            # data=customerdetailsdb.objects.filter(username=username_c,password=password_c).values('email','id').first()
            request.session['username']=username_c
            request.session['password']=password_c
            # request.session['email'] =data['email']
            # request.session['userid'] =data['id']
            return redirect(homepage)
        else:
            return render(request,"CustomerLogin.html",{'msg':"sorry..Invalid Username or Password"})
def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect (homepage)
def savecontact(request):
    if request.method == "POST":
        yn = request.POST.get('contactname')
        ye = request.POST.get('contactemail')
        ys = request.POST.get('subject')
        ym = request.POST.get('message')
        obj = contactdb(Cname=yn,Cemail=ye,Subject=ys,Message=ym)
        obj.save()
        return redirect(contactpage)



