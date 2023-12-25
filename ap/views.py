from django.shortcuts import render
from .form import userform
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import ser,Tavarlar,saqlash
from django_htmx.http import HttpResponseLocation
# Create your views here.
def elektron(request):
    return render(request,'elektron.html')
def reg(request):
    fro=userform()
    if(request.method=='POST'):
        fro=userform(request.POST)
        if fro.is_valid():
            use=fro.save()
            login(request,use)
            return redirect('elktr')
    for i in fro:
        if(i.label=='Password'):
            i.label='Parol'
        if i.label=='Password confirmation':
            i.label='Parol tekshirish'
    return render(request,'royhat.html',{'fro':fro})

def kirish(request):
    if request.method=='POST':
        ism=request.POST['ism']
        parol=request.POST['parol']
        data=authenticate(request,username=ism,password=parol)
        if  data is not None:
            login(request,data)
            return redirect('elktr')
        else:
            print('xatolik')
    return render(request,'kirish.html')
def chiq(request):
    logout(request)
    return redirect('elktr')

def tavarlar(request):
    if request.htmx:
        return HttpResponseLocation('div_addd/',target='nlp')
    s=Tavarlar.objects.all()
    user=ser.objects.get(username=request.user)
    saq= saqlash.objects.filter(kim=request.user.username)

    return render(request,'tavarlar.html',{'tavarlar':s,'user':user,'saq':saq})

def save_add(request,id):
    t=Tavarlar.objects.get(id=id)
    saq=saqlash.objects.filter(s_nomi=t.nomi,s_rasmi=t.rasmi,narxi=t.narxi)
    if saq:
        saq.delete()
    else:
        saqlash.objects.create(s_nomi=t.nomi,s_rasmi=t.rasmi,narxi=t.narxi,kim=request.user.username)
    return redirect(request.META.get("HTTP_REFERER"))
def div_addd(request):
    return render(request,'add_card.html')
def div_x(request):
     return render(request,'tavarlar.html')

def save_x(request,id):
    saq=saqlash.objects.get(id=id)
    saq.delete()
    return redirect(request.META.get("HTTP_REFERER"))
def add(request):
    if request.method=='POST':
        nomi=request.POST['nomi']
        rasmi=request.FILES['rasmi']
        narxi=request.POST['narxi']
        kim=request.user.username
        Tavarlar.objects.create(nomi=nomi,rasmi=rasmi,narxi=narxi,kim=kim)
        return redirect('tavarlar')
    return render(request,'add.html')

def post_delet(request,id):
    t=Tavarlar.objects.filter(id=id,kim=request.user.username)
    if t:
        t.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def tavar_i(request):
    if request.method=='POST':
      ni=request.POST['ni']
      tavar=Tavarlar.objects.filter(nomi__icontains=request.POST['ni'])
    return render(request,'tavar_i.html',{'t_i':tavar})
    
