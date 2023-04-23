from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm,CustomAuthenticationForm,CustomUserChangeForm,CustomPasswordResetForm
from django.http import HttpResponse
from django.contrib import messages
from .models import CustomUser
from .email_settings import send_forget_password_mail
import uuid


def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            messages.success(request,"Account Created Successfully")
            user_form.save()
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        user_form=CustomUserChangeForm(request.POST,instance=request.user)
        if user_form.is_valid():
            messages.success(request,"Profile updated Successfully")
            user_form.save()
            return redirect('/profile/')

    user_form=CustomUserChangeForm(instance=request.user)
    return render(request,'app/update_profile.html',{'form':user_form})

def user_pass_change(request,token):
    context = {}
    
    
    try:
        profile_obj = CustomUser.objects.filter(forget_password_token = token).first()
        import ipdb
        # ipdb.set_trace()
        context = {'user_id' : profile_obj.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                         
            
            user_obj = CustomUser.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request, 'Your Password has been changed')
            # return redirect('/login/')
            
    except Exception as e:
        print(e)
    return render(request , 'app/change-password.html' , context)


def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not CustomUser.objects.filter(email=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
            
            user_obj = CustomUser.objects.get(email = username)
            token = str(uuid.uuid4())
            user_obj.forget_password_token = token
            user_obj.save()
            send_forget_password_mail(user_obj , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')
    except Exception as e:
        print(e)
    return render(request , 'app/forget-password.html')            
    
    
def logout_view(request):
    logout(request)
    return redirect('/login/')

def home(request):
    if request.user.is_authenticated:
        user=request.user
        return render(request,'app/home.html',{'user':user})
    else:
        return redirect('login')