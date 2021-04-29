# here we are importing the request module to deal with our HTTP functionalities
import requests
# this library automatically takes a search and turns the string into a usable url
from requests.compat import quote_plus
from django.shortcuts import render
# here we are importing Beautiful Soup which is used for web scraping
from bs4 import BeautifulSoup
# to access the database we import our models
from . import models

BASE_CRAIGSLIST_URL = 'https://inlandempire.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

# Create your views here.
# when this funcion is called, it renders the base.html in templates
def home(request):
    return render(request, 'base.html')

# this fuction returns the result of the search page when ther is a new search
def new_search(request):
    # this is pulling out the data from when the submit button is pressed
    search = request.POST.get('search')
    # we create an object of Search and place that object in our new_search function
    models.Search.objects.create(search=search)
    # using string concatination on the string that was input by the user,
    # we can get our final url
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    # what this does is gets all the html data from the url that was passed in
    data = response.text
    # this is parsing the data and creating a beautifulsoup object which encapsulates all the 
    # html data into its tags in nested parts instead of a raw string of html
    soup = BeautifulSoup(data, features='html.parser')
    # by inspecting the html of a search in craigslist we are able to retrieve the necessary
    # data we need to display on our webpage
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []
    
    # throughout this loop we are parsing the html search results and filtering out different 
    # result cases which is based on whatever the user searches
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'
        
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_postings.append((post_title, post_url, post_price, post_image_url))
    # post_title = post_listings[0].find(class_='result-title').get_text()
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find(class_='result-price').text

    # print(data)
    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)