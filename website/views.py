from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signUpForm, addRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In !")
            return redirect('home')
        else:
            messages.success(request, "There was an error while loggin in, Please Try again !")
            return redirect('home')
    else: 
        return render(request, 'home.html', {'records': records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login with registered info 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"You have successfully registered as {username}")
            return redirect('home')
        
    else:
        form = signUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})

    else:
        messages.success(request, 'You must be logged in to view this page')
        return render(request, 'home.html')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record is Deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You need to be logged in to do that !!")
        return redirect('home')
    
def add_record(request):
    form = addRecordForm(request.POST)
    if request.user.is_authenticated:
        if request.method == 'POST' or None:
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Successfully")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You need to be logged in for that operation")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = addRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    
    else:
        messages.success(request, "You need to be logged in for that operation")
        return redirect('home')

