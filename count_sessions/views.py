from django.shortcuts import render, redirect, HttpResponse
def index(request):
    if "counter" not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return render(request,'index.html')

def destroy(request):
    if request.session['counter'] > 10 : 
        del(request.session['counter'])
    return redirect('/')

