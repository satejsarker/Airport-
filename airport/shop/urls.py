from django.conf.urls import url
from django.views.generic import ListView,DetailView
from shop.models import shop

urlpatterns = [
    url(r'^$',ListView.as_view(queryset=shop.objects.all().order_by("title")[:20],template_name="shop/shop.html")),
    url(r'^(?P<pk>\d+)$',DetailView.as_view(model=shop,template_name = 'shop/shop1.html'))
]