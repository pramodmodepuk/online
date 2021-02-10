from django.urls import path
from . import views

app_name = "online"
urlpatterns = [
    path("", views.auth_view, name='login'),

]