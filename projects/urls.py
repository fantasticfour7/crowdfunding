from django.conf.urls import url
from . import views

app_name = "projects"
urlpatterns = [
    url(r'^search',views.user_search,name = "search"),
    url(r'^dev-dash',views.DevDash.as_view(),name='dev-dash'),
    url(r'^invest-dash',views.InvestDash.as_view(),name='invest-dash'),
]