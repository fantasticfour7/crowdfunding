from django.conf.urls import url
from . import views

app_name = "projects"
urlpatterns = [
    url(r'^search',views.user_search,name = "search"),
    url(r'^new-project',views.DevDash.as_view(),name='dev-dash'),
]