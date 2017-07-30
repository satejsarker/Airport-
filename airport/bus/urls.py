from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from bus.models import bus
urlpatterns=[
    url(r'^$',ListView.as_view(queryset=bus.objects.all().order_by("dep")[:20],template_name="bus/bus.html"))
    ]
   
    
# Create your views here.

