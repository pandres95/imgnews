from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render_to_response('base.html', { 'authenticated': False } )