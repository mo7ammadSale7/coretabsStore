from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone



# Create your views here.
def say_hi(request, name):
    return render(request, 'say-hi.html', {'name': name})

def show_time(request):
    now = timezone.now()
    return render(request, 'show-time.html', {'now': now})
