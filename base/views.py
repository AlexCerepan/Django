from django.http import HttpResponse
from django.shortcuts import render

# data
rooms = [
    {'id':1, 'name': 'Alex'},
    {'id':2, 'name': 'Matus'},
    {'id':3, 'name': 'Pato'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')
