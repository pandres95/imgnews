from django.shortcuts import render, render_to_response

# Create your views here.
def inicio(request):
    return render_to_response('init.html', { 'authenticated': True, 'title': 'Inicio' } )