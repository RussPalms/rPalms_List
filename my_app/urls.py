from django.urls import path
# in here we are calling our views functionality
from . import views

urlpatterns = [
    # if the path match is empty, run the home function from views
    path('', views.home, name='home')
]