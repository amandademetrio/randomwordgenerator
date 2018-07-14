from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    random_dict = {
        'word': get_random_string(length=14)
    }
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    print("counter is :",request.session['counter'])
    return render(request,'randomwordapp/index.html',random_dict)

def destroy(request):
    request.session['counter'] = 0
    return redirect('/')