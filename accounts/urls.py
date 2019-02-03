from django.conf.urls import url
from . import views
from projects.views import project_form

app_name = 'accounts'

urlpatterns = [
    url(r'^investor-sign-up/$',views.InvestorSignUpView.as_view(), name='Investor-SignUp'),
    url(r'^dev-sign-up/$',views.DeveloperSignUpView.as_view(), name='User-SignUp'),
    url(r'^sign-up/$',views.UserSignUpView.as_view(), name='SignUp'),
    url(r'^redirecting/$',views.redirectview, name='dummy'),
    url(r'^login/',views.login_page, name = "login"),

]