from django.urls import path
from . import views

urlpatterns = [
    # as_view renders the class as a view
    # Method is only needed in class based views
    path("", views.MenuList.as_view(), name="home"),

]
