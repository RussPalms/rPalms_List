from django.db import models

# Create your models here.
# This model gives us the search fuctionality of our application
class Search(models.Model):
    # here we are defining the maximum length of the input 
    # our user can give
    search = models.CharField(max_length=500)
    # we then define the exact time a search is made
    created = models.DateTimeField(auto_now=True)

    # this functions is making sure our search model outputs a string 
    # of searches
    def __str__(self):
        return '{}'.format(self.search)

    # After creating a superuser using python manage.py createsuperuser
    # we can log into our admin account and look at the searches that 
    # were made. Initially the output that represents our 'Search' 
    # function is 'Searchs' with this subclass we are defining 
    # that 'Searchs' object to be 'Searches' 
    class Meta:
        verbose_name_plural = 'Searches'