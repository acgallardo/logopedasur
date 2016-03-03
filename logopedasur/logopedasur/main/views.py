from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response


# Create your views here.

@login_required(login_url="/login/")
def index(request):
    return render_to_response("main/index.html",
            {"nombre": "trukise"},
            context_instance=RequestContext(request))


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['from']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return render_to_response("main/login.html",
                                          {"error":"disabled", "message":"La cuenta esta deshabilitada"},
                                          context_instance=RequestContext(request))
        else:
            return render_to_response("main/login.html",
                                      {"error":"login", "message":"El nombre de usuario no existe"},
                                      context_instance=RequestContext(request))
    else:
        return render_to_response("main/login.html",
                              {"error":"", "message":""},
                              context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('index'))
