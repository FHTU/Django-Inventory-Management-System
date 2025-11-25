from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member,Per
from time import time 

def req (req) :

    usna = req.POST.get('usn')
    pasw = req.POST.get('psw')
    m = req.POST.get('mode')
    obj = Per.objects.filter(usn=usna)
    state = ''

    try :
        if req.session['login'] and m == 'o': return redirect('order')
        elif req.session['login'] and m == 's'  : return redirect('show')
        else : req.session.flush()
    except :
        req.session.clear_expired()
        req.session['login'] = False
        req.session.set_expiry(10*60*60)

    try :
        passwo = obj.all().values()[0]['psw']
        if pasw == passwo :
            if m =='o':
                req.session['login'] = True
                return redirect('order')
            elif m == 's':
                req.session['login'] = True
                return redirect('show')
        else :
            state = 'wrong password'
            
    except : pass

    temp = loader.get_template('index.html')
    return HttpResponse(temp.render({'state':state},req))

def show(req):

    try :
        if req.session['login'] == False :
            return redirect('req')
    except :
        return redirect('req')
    
    mode = req.POST.get('mode')
    code = req.POST.get('code')
    name = req.POST.get('name')
    amount = req.POST.get('amount')
    
    if (code and name and amount and mode =="add") :
        obj = Member.objects.filter(code=code)
        if not obj.update(name=name,amount=amount):
            Member(code=code,name=name,amount=amount).save()

        print(code,name,amount)
        
    elif (code and mode =="remove") :
        obj = Member.objects.filter(code=code)
        obj.delete()

    else : pass


    value = Member.objects.all().values()
    temp = loader.get_template('show.html')
    show = temp.render({'code':code,'name':name,'amount':amount,'data':value},req)
    return HttpResponse(show)

def order(req):
    
    try :
        if req.session['login'] == False :
            return redirect('req')
    except :
        return redirect('req')
    
    mode = req.POST.get('mode')
    code = req.POST.get('code')
    name = req.POST.get('name')
    amount = req.POST.get('amount')

    if (mode == "order") :
        obj = Member.objects.filter(code=code)
        obj.update(name=name,amount=amount)

    elif (mode == "search") :
        try :
            obj = Member.objects.get(code=code)
            name = obj.name
            amount = obj.amount
        except :
            return HttpResponse("Search failed")
    elif (mode == None) :
        pass
    else :
        return HttpResponse("Unecxepted Error Occurced")

    temp = loader.get_template('det.html')
    return HttpResponse(temp.render({'value':{'code' : code , 'name' : name , 'mount' : amount}},req))

def error_404_view(request, exception):
    temp = loader.get_template('404.html')
    return temp.render(request, '404.html')

