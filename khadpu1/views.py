from django.shortcuts import render , HttpResponse
from .models import Images , Gallery , Politics,text_info , Login 
from django.contrib import messages
from django.db.models import Q
import random
import requests

def frontpage(request):
    # if request.method == 'POST':
    #     query = request.POST.get('query')
    #     places_for = Images.objects.filter(
    #         Q(name__icontains=query) | Q(state__icontains=query)
    #     )
    #     return render(request , 'search_items.html' , {'place':places_for})
    image = Images.objects.all().order_by('-id')
    context = {
        'places':image,
    }
    request.session['login'] = 'False'
    return render(request , 'homepage.html' , context)
    
def gallery(request):
    returned  = Gallery.objects.all().order_by('-id').order_by('-id')
    context = {
        'pictures':returned,
    }
    request.session['login'] = 'False'
    return render(request , 'gallery.html',  context)
def add(request):
    if 'login' not in request.session or request.session['login'] != 'True':
        return login(request)
        
    if request.method == 'POST':
        # images = Images(name = request.POST.get['name'] , image = request.FILES['image'] , description = request.POST.get['desc'])
        images = Images()
        images.name = request.POST.get('name')
        images.image = request.FILES['image']
        images.description = request.POST.get('desc')
        images.location = request.POST.get('location')
        images.type = request.POST.get('type')
        images.save()
        if images.save():
            messages.success(request ,'Data added')
    context = {
            'messages':messages
        }       
    return render(request , 'renamed.html' , context)   
def add_gallery(request):
    if 'login' not in request.session or request.session['login'] != 'True':
        return login(request)
    if request.method == 'POST':
        gallery = Gallery()
        gallery.image = request.FILES['image']
        gallery.name = request.POST.get('name')
        gallery.save()
        if gallery.save():
            messages.success(request , 'Picture added')
    context = {
            'messages':messages
        }        
    return render(request , 'add_gallery.html' , context)    
     
def destinations(request):
    places = Images.objects.all().order_by('-id')
    request.session['login'] = 'False'
    
    type_mappings = {
        'Mandir': 'mandir',
        'Places': 'Places',
        'Learning': 'learning',
        'Healthcare': 'health',
        'Library': 'library',
        'Yoga': 'Yoga',
        'Hotels': 'hotel',
        'Grocessory': 'gro',
        'Bridge': 'bridge',
        'others': 'others',
    }
    
    type_d = list(type_mappings.keys())
    
    context = {
        'places': places,
        'type': type_d,
    }
    
    for type_name, type_field in type_mappings.items():
        context[type_field] = Images.objects.filter(type=type_name).order_by('-id')
    
    return render(request, 'destinations.html', context)

def navbar(request):
    return render(request , 'main_navbar.html')    
def politics(request):
    request.session['login'] = 'False'
    people = Politics.objects.all().order_by('-id').order_by('-id')
    context = {
        'people':people,
    }    
    return render(request , 'politics.html' , context)
def add_politics(request):
    if 'login' not in request.session or request.session['login'] != 'True':
        return login(request)
    if request.method == 'POST':
        r = request.POST
        people = Politics(name = r.get('name') , about_khadpu = r.get('about') , facebook = r.get('facebook') , position = r.get('position') , image = request.FILES['image'] )
   
        people.save()
    return render(request , 'add_politics.html')    
# Create your views here.
def add_text(request):
    if 'login' not in request.session or request.session['login'] != 'True':
        return login(request)
    if request.method == 'POST':
        r=request.POST 
        
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            
            text = text_info(image=image_file, name=r.get('title'), info_text=r.get('description'))
        else:
            text = text_info(name=r.get('title'), info_text=r.get('description'))        
        text.save()
    return render(request , 'add_text.html')    
def more_info(request):
    request.session['login'] = 'False'
    textinfo = text_info.objects.all().order_by('-id')
    context = {
    'text_info':textinfo , 
    
    }
    return render(request , 'more_info.html' , context)
from django.shortcuts import render
from .models import Images, Gallery, Politics, text_info

def data_view(request):
    images = Images.objects.all().order_by('-id')
    gallery = Gallery.objects.all().order_by('-id')
    politics = Politics.objects.all().order_by('-id')
    text_infos = text_info.objects.all().order_by('-id')

    context = {
        'images': images,
        'gallery': gallery,
        'politics': politics,
        'text_infos': text_infos,
    }

    return render(request, 'data_display.html', context)
def login(request):
    admin = "admin"
    if not Login.objects.filter(username=admin).exists():
        cred = Login(username = 'admin' , password = 'admin')
        cred.save()
    if request.method == 'GET' and request.GET.get('username') == 'admin':
        r = request.GET
        username = r.get('username')
        password = r.get('password')
        try:
            if Login.objects.filter(username =username, password = password):
            
                request.session['login']= 'True'
                return add_text(request)
            else:
                return loading(request)  
        except:
            return loading(request) 
    return render(request , 'login.html' , {'data':Login.objects.all().order_by('-id')})   
def loading(request):
    return render(request , 'loading.html')    


from django.shortcuts import render

def timeline(request):
    monthNamesNepali = [
        'बैशाख', 'जेठ', 'अषाढ', 'श्रावण', 'भाद्र', 'आश्विन',
        'कार्तिक', 'मंसिर', 'पौष', 'माघ', 'फाल्गुण', 'चैत्र'
    ]

    days_in_month = list(range(1, 32))
    
    context = {
        'monthNamesNepali': monthNamesNepali,
        'days_in_month': days_in_month,
    }
    
    return render(request, 'timeline.html', context)

def customize(request):
    if 'login' not in request.session or request.session['login'] != 'True':
        return login(request)
    images = Images.objects.all().order_by('-id')
    gallery = Gallery.objects.all().order_by('-id')
    politics = Politics.objects.all().order_by('-id')
    Text_info = text_info.objects.all().order_by('-id')

    context = {
        'images': images,
        'gallery': gallery,
        'politics': politics,
        'text_info': Text_info,
    }

    
    

    return render(request, "customize.html" , context)
database = [Images, Gallery, Politics, text_info, Login]  # Assuming these are your model classes

def true_customize(request):
    r = request.POST
    model_class_name = r.get('model')
    id = r.get('id')
    if model_class_name == "Images":
        
        try:
            item = Images.objects.get(id=id)
            item.delete()
            return JsonResponse({"data": "Changed"})
        except:
            return JsonResponse({"data": "Invalid input"})
    elif model_class_name == "Gallery":
        try:
            item = Gallery.objects.get(id=id)
            item.delete()
            return JsonResponse({"data": "Changed"})
        except:
            return JsonResponse({"data": "Invalid input"})
    elif model_class_name == "Politics":
        try:
            item = Politics.objects.get(id=id)
            item.delete()
            return JsonResponse({"data": "Changed"})
        except:
            return JsonResponse({"data": "Invalid input"})
    elif model_class_name == "text_info":
        try:
            item = text_info.objects.get(id=id)
            item.delete()
            return JsonResponse({"data": "Changed"})
        except:
            return JsonResponse({"data": "Invalid input"})
    
    else:
        return JsonResponse({"data": "Invalid input"})
    
def change_info(request , model , id):
    
    r=request.POST
    model_class_name = model
    id = id
    if model_class_name == "Images":
       
        if request.method == 'POST':
        # images = Images(name = request.POST.get['name'] , image = request.FILES['image'] , description = request.POST.get['desc'])
            images = Images.objects.get(id = id)
            images.name = request.POST.get('name')
            
            try:
                if request.FILES['image'] != '':
                    images.image =  request.FILES['image'] 
            except:
                ui = images.image
            images.description = request.POST.get('desc')
            images.location = request.POST.get('location')
            images.type = request.POST.get('type')
            images.save()
        return render(request , 'change_info.html' , {'data':Images.objects.get(id=id)})
           
        
    elif model_class_name == "Gallery":
        
        if request.method == 'POST':
            gallery = Gallery.objects.get(id=id)
            try:
                if request.FILES['image'] != '':
                    gallery.image =  request.FILES['image'] 
            except:
                ui = gallery.image
            gallery.name = request.POST.get('name')
            gallery.save()
           
        return render(request , 'change_info.html' , {'data':Gallery.objects.get(id=id)})
            
    elif model_class_name == "Politics":
       
        if request.method == 'POST':
            people = Politics.objects.get(id=id)
            people.name = r.get('name')
            try:
                if request.FILES['image'] != '':
                    people.image =  request.FILES['image'] 
            except:
                ui = people.image
            people.about_khadpu = r.get('about')
            people.facebook = r.get('facebook')
            people.position = r.get('position')
            
           
            people.save()
        return render(request , 'change_info.html' , {'data':Politics.objects.get(id=id)})       
        
    elif model_class_name == "text_info":
        if request.method == 'POST':
            text_image = text_info.objects.get(id=id)
            
            try:
                if request.FILES['image'] != '':
                    image_file = request.FILES['image']
            except:
                image_file = text_image.image
            text = text_info.objects.get(id = id)
            text.delete()
            
            text = text_info(id=id, image=image_file, name=r.get('name'), info_text=r.get('info_text'))
            text.save()
            
        return render(request , 'change_info.html' , {'data':text_info.objects.get(id=id) , 'text':'true'})  
              
          
    else:
        return HttpResponse('thankyou')
      




    