from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Users.models import User
from Codm.models import Cart
from .forms import UserCreationForm

def LoginFunc(request):
    Page = 'login'
    message = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try: 
            user = User.objects.get(email=email)
        except:
            message = "Something is Wrong!"
        else:
            USER = authenticate(request, email=email, password=password)

            if USER:
                login(request, USER)
                message = "You Successfully logged in!"
                return redirect('Codm:home')
            else:
                message = "Something is Wrong! Check the Username And Password"
    final_message = message if message != None else ''
    context = {
        'message' : final_message,
        'Page' : Page,
    }
    return render(request, 'Codm/login.html', context)
def LogoutFunc(request):
    logout(request)
    return redirect('Codm:home')

def RegisterFunc(request):
    user_form = UserCreationForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            cart = Cart(user=user, status='fn')
            cart.save()
            login(request, user)
            message = "You Successfully logged in!"
            return redirect('Codm:home')
    return render(request, 'Codm/signup.html', {'form' : user_form})