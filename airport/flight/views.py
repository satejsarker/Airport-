from django.shortcuts import render

def index(request):
    return render(request, 'flight/flight.html')
def taxi1(request):
    return render(request,'flight/taxi1.html')
def rentcar(request):
    return render(request,'flight/rentcar.html')