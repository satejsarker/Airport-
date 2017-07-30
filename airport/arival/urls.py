from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from arival.models import arival

# Create your views here.
urlpatterns=[
 url(r'^$',ListView.as_view(queryset=arival.objects.all().order_by("-sta")[:20],template_name="flight/arival.html"))
]