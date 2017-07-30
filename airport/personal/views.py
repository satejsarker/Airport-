from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')
def content(request):
    return render(request,'personal/content.html',{'content':["this is page for basic python value passing "]})
