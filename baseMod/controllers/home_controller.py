from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf

# Create your views here.
def inicio(request):
    c = { 'user' : request.user, 'authenticated': request.user.is_authenticated(), 'title': 'Inicio' }
    c.update(csrf(request))

    return render_to_response('home/init.html', c)
