from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):  # we can't call it login because it will conflict with built-in function
	records=Record.objects.all()
	#if user is sumitting form its POST request
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,'You are now logged in!')
			return redirect('home')
		else:
			messages.error(request,'There was a error login in , please try again')
			return redirect('home')
	else:
		return render(request,'home.html',{'records':records})#already submitted , viewing the page
    

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})
def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def logout_view(request):
      logout(request)
      return redirect("/")

def customer_record(request,pk):
	if request.user.is_authenticated:
		#look up records
		customer_record=Record.objects.get(id=pk)
		return render(request,'record.html',{'customer_record':customer_record})
	else:
		messages.success(request,'You are not logged in')
		return redirect('home')
	

def delete_record(request,pk):
	if request.user.is_authenticated:
		#look up records
		customer_record=Record.objects.get(id=pk)
		customer_record.delete()
		messages.success(request,'Record Deleted Successfully ...')
		return redirect('home')
	else:
		messages.success(request,'You are not logged in')
		return redirect('home')
	
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				add_record = form.save()
				messages.success(request,'Record Added Successfully ...')
				return redirect('home')
		return render(request,'add_record.html',{'form':form})
	else:
		messages.success(request,'You are not logged in')
		return render(request,'add_record.html',{})
	
def update_record(request,pk):
	if request.user.is_authenticated:
		#look up records
		current_record=Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if request.method == 'POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Record Updated Successfully ...')
				return redirect('home')
		return render(request,'update_record.html',{'form':form})
	else:
		messages.success(request,'You are not logged in')
		return redirect('home')