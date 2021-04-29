from django.shortcuts import render

# Create your views here.
# when this funcion is called, it renders the base.html in templates
def home(request):
    return render(request, 'base.html')