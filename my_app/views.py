from django.shortcuts import render

# Create your views here.
# when this funcion is called, it renders the base.html in templates
def home(request):
    return render(request, 'base.html')

# this fuction returns the result of the search page when ther is a new search
def new_search(request):
    # this is pulling out the data from when the submit button is pressed
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)