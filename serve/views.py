from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .models import Car
from .models import Booking
from . import forms



# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return render(request,'index.html')
 
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})



def gallery(request):
    #return HttpResponse("UG")
    cars = Car.objects.all()
    
    return render(request,'gallery.html',{'cars':cars})

def book(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    total_cost = None

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        total_cost = quantity * car.price

 # Create a new Booking object and save it to the database
        booking = Booking.objects.create(car=car, quantity=quantity, total_cost=total_cost)
        
        return redirect('gallery')

    return render(request, 'book.html', {'car': car, 'total_cost': total_cost})

def contact(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for interacting with our website!")
   
            #return redirect('home') 
    else:
       form = forms.PostForm()
    return render(request, 'contact.html', {'form':form})


def about(request):
    #return HttpResponse("UG")
    return render(request,'about.html')

def services(request):
    #return HttpResponse("UG")
    return render(request,'services.html')

