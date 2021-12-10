from django.contrib.auth import authenticate,login,logout
from django.contrib.messages.api import warning
# from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm ,EditUserprofileForm,CreateBookForm
from ems.models import Event,Sponsor,News,Booking

# Create your views here.
def index(request):
    
    if request.user.is_anonymous:
        return redirect("loginUser")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            # warning error info success 
            messages.error(request,'Please Enter Proper Username and Password')
            return render(request, 'login&out.html')
            
    return render(request, 'login&out.html')

def logoutUser(request):
    logout(request)
    return redirect("loginUser")
      


def registerUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user= authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect(loginUser)
    else:
        form=CreateUserForm()
    return render(request,'login&out.html',{'form':form})   


@login_required(login_url="/login/") 
def profile(request):
    context={
        'user':request.user
    }
    return render(request,'profile.html',context)


@login_required(login_url="/login/") 
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            fm=EditUserprofileForm(request.POST,instance=request.user)
            if fm.is_valid():
                # messages.success(request,"updated !!")
                fm.save()
        else:
            
            fm=EditUserprofileForm(instance=request.user)
        
        return render(request,'edit_profile.html',{'form':fm})

    else:
        return render(request, 'login&out.html')
  
      
@login_required(login_url="/login/")  
def eventsview(request):
    allevents=Event.objects.all()
    # for item in allevents:
    #     print(item.Event_sponsor)
    context={'eventsview':allevents}
    return render(request, 'event.html',context)


@login_required(login_url="/login/") 
def news(request):
    
    allnews=News.objects.all()
    context={'allnews':allnews}
    return render(request,'news.html',context)
    



# seperate admin panel

def manage(request):
    # context={'success':False}
    # if request.method == 'POST':
    #     Event_name=request.POST['Event_name']
    #     Event_category=request.POST['Event_category']
    #     # Event_Desc=request.POST['Event_Desc']
    #     Event_sponsor=request.POST['Event_sponsor']
    #     Event_price=request.POST['Event_price']
    #     Event_venue=request.POST['Event_venue']
    #     Event_datetime=request.POST['Event_datetime']
    #     # Event_image=request.POST['Event_image']
    #     ins=Event(Event_name=Event_name,Event_sponsor=Event_sponsor,Event_category=Event_category,Event_price=Event_price,Event_venue=Event_venue,Event_datetime=Event_datetime)
    #     ins.save()
        
    #     context={'success':True}
    return render(request,'Admin/admin.html')


@login_required(login_url="/login/") 
def booking(request):
    
    user=request.user    
    allbooking=Booking.objects.filter(Booking_username=user)
        
    # for item in allbooking:
    #     print(item.Booking_username)
    context={'allbooking':allbooking}
    
    # context={'success':False}
    
    # if request.method == 'POST':
        
    #     Booking_event=request.POST['Booking_event']
    #     Booking_member=request.POST['Booking_member']
    
    
    #     ins=Booking(Booking_event=Booking_event,Booking_member=Booking_member)
    #     ins.save()
        
    #     context={'success':True}
      
    return render(request,'booking.html',context)

def delete_booking(request,id):
    
    if request.method == 'POST':
        de=Booking.objects.get(pk=id)
        de.delete()
        return redirect(booking)
    # return render(request,'booking.html')   
        

@login_required(login_url="/login/") 
def bookform(request,id):
    event=Event.objects.filter(id=id).first()
    book_form=CreateBookForm()   
    if request.method == 'POST':  
        book_form=CreateBookForm(request.POST)       
        if book_form.is_valid():          
            book_form.save()
            return redirect("booking")  
    
    # context={'success':False}
    
    # if request.method == 'POST':
        
    #     Booking_username=request.POST['Booking_username']
    #     Booking_event=request.POST['Booking_event']
    #     Your_name=request.POST['Your_name']
    #     Your_phone=request.POST['Your_phone']
    
    
    #     ins=Booking(Booking_username=Booking_username,Booking_event=Booking_event,Your_name=Your_name,Your_phone=Your_phone)
    #     ins.save()
        
    #     context={'success':True}
        
    return render(request,'Bookform.html',{'book_form':book_form,'event':event})

