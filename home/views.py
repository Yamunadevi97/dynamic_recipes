from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from home.forms import ContactForm

def home(request):
    return render(request, 'index.html')     #static webpage
# views.py

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = ContactForm()
    
    return render(request, 'home/contact.html', {'form': form})


# views.py

# views.py
from django.shortcuts import render

def about(request):
    return render(request, 'home/about.html')
def new(request):
    return render(request, 'home/new.html')
def success_page(request):
    return HttpResponse('<h1>Hey this is a success page</h1>')
from django.shortcuts import render
def pizza(request):
	return render (request,'rec/pizza.html')
def burger(request):
	return render (request,'rec/burger.html')
def noodles(request):
	return render (request,'rec/noodles.html')
def sandwich(request):
	return render (request,'rec/sandwich.html')
def gravy(request):
	return render (request,'rec/gravy.html')
def soup(request):
	return render (request,'rec/soup.html')

# Create your views here.
