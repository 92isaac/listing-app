from django.urls import path
from django.http import HttpResponse
from . import views


# def home(request):
#     return HttpResponse("<div><h1>This is our real estate Home page</h1> <p>I love django</p></div>")

# def about(request):
#     return HttpResponse("<h1>This is our real estate About page</h1>")

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name="about"),
    path('agent_list/', views.agent_list, name="agent_list"),
    path('list_details/<pk>/', views.list_detail, name="list_details"),
    path('create_card/', views.create_form, name="create_card"),
    path('update_card/<pk>/', views.update_form, name="update_card"),
    path('delete/<pk>/', views.delete, name="delete"),
]