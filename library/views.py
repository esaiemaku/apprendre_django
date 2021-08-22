
from django.shortcuts import render
from .models import Book


def index(request):
 books=Book.objects.all()
 
 context={ 'Books':Book}

 return render(request, 'library/index.html', context)

# Create your views here.
