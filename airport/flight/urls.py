from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from flight.models import flight
from .import views
urlpatterns=[
    url(r'^$',ListView.as_view(queryset=flight.objects.all().order_by("sta")[:20],template_name="flight/flight.html")),
    url(r'^taxi1/',views.taxi1, name='airporttaxi'),
    url(r'^rentcar/',views.rentcar,name='rentcar')
    ]