from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView
from .models import UserProject, Domain_Choices
from accounts.models import CustomUser
from django.http import request, HttpRequest
from .forms import UserProjectForm
from accounts.models import CustomInvestor


domain_list = Domain_Choices
def project_form(request):
    if request.method == 'POST':
        project_name = request.POST["project_name"]
        funds = request.POST["funds"]
        domain = request.POST["domain"]
        description = request.POST["description"]
        contributors = request.POST["contributors"]
        ongoing = bool(request.POST.get("ongoing"))
        print(ongoing)
        obj = UserProject(name = project_name, funds_Required = funds, domain = domain, Project_Description = description, contributors = contributors, ongoing = ongoing)
        obj.save()
        print(obj)
    return render(request,'accounts/student.html',{ "domain" : domain_list})

def user_search(request):
    req = request.method
    if req == "POST":
        val = True
        print(request.POST.get('squery'))
        results = UserProject.objects.filter(name__startswith = request.POST.get("squery"))
        return render(request, 'projects/search.html',{ "results" : results, "val": val})
    else:
        val = False
        return render(request, 'projects/search.html', {"val" : val})

class DevDash(CreateView):
    model = UserProject
    template_name = 'accounts/student.html'
    form_class = UserProjectForm
    context_object_name = 'projects'

    def post(self,request):
        if request.method == 'POST':
            print(request.user)
            form = UserProjectForm(request.POST, request.FILES)
            print('hi')
            if form.is_valid():
                new_flow=form.save(commit=False)
                new_flow.owner = CustomUser.objects.get(username__startswith = request.user)
                print(new_flow)
                new_flow.save()
                return redirect('projects:dev-dash')
            else:
                print(form.errors)

class InvestDash(ListView):
    model = CustomInvestor
    template_name = 'accounts/Investor.html'
    context_object_name = 'investor'
    def get_queryset(self):
        return CustomInvestor.objects.all()
    
