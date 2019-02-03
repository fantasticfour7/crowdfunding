from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import CustomInvestorCreationForm, CustomDeveloperCreationForm, CustomUserCreationForm
from .models import CustomUser, CustomDeveloper, CustomInvestor

class InvestorSignUpView(CreateView):
    form_class = CustomInvestorCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/InvestorSignUp.html' 
    
    def post(self,request):
        print("Hi")
        print(request.session['user'])
        user = CustomUser.objects.get(username__startswith = request.session['user'])
        if request.method == 'POST':
            form = CustomInvestorCreationForm(request.POST)
            if form.is_valid():
                new_flow=form.save(commit=False)
                new_flow.user = user
                print(new_flow)
                new_flow.save()
                return redirect("accounts:login")
            else:
                print("Invalid form")
                print(form.errors)

class DeveloperSignUpView(CreateView):
    form_class = CustomDeveloperCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/DeveloperSignUp.html' 

    def post(self,request):
        print("Hi")
        print(request.session['user'])
        user = CustomUser.objects.get(username__startswith = request.session['user'])
        if request.method == 'POST':
            form = CustomDeveloperCreationForm(request.POST)
            if form.is_valid():
                new_flow=form.save(commit=False)
                new_flow.user = user
                print(new_flow)
                new_flow.save()
                return redirect("accounts:login")
            else:
                print("Invalid form")
                print(form.errors)


class UserSignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html' 

    def post(self,request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            pass1 = request.POST['password1']
            pass2 = request.POST['password2']
            if pass1 == pass2:
                print(form)
                print("Ji")
                if form.is_valid():
                    print("HI")
                    form.full_clean()
                    new_flow=form.save(commit=False)
                    user=new_flow.username
                    print(new_flow)
                    new_flow.save()
                    request.session['user'] = user 
                    return redirect('accounts:dummy')
            return redirect('accounts:SignUp')
    


def redirectview(request):
    print(request.session['user'])
    user = CustomUser.objects.get(username__startswith = request.session['user'])
    print(user)
    print(user.user_type)
    if user.user_type == 'A':
        return redirect('accounts:Investor-SignUp')
    else:
        return redirect('accounts:User-SignUp')



def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        # print(form)
        if form.is_valid():
            print("----HI----")
            user = form.get_user()
            print(user)
            login(request, user)    
            if user.user_type == 'A':
                return redirect('projects:invest-dash')
            return redirect('projects:dev-dash')
    else:
        form = AuthenticationForm()
        return render (request, "accounts/login.html", {"form" : form})

def index_page(request):
    return render(request,"index.html")
