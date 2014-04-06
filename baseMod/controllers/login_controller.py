from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")

def login_(request):
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
    else:
        username, password = request.GET['username'], request.GET['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/")
        else:
            # Return a 'disabled account' error message
            return HttpResponseRedirect("/")
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect("/")
