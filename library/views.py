
from django.shortcuts import render
from .models import Boooks
from.models import user_name

def index(request):

    context={'Boooks':Boooks,'user_name':user_name}
    return render(request, 'library/index.html',context)


# Create your views here.
