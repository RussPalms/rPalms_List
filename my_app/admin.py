from django.contrib import admin
# in here we are calling our Search model
from .models import Search

# Register your models here.
admin.site.register(Search)