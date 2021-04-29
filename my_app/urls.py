from django.urls import path
# in here we are calling our views functionality
from . import views

urlpatterns = [
    # if the path match is empty, run the home function from views
    path('', views.home, name='home'),
    # this is the path when a new search is activated
    path('new_search', views.new_search, name='new_search')
]