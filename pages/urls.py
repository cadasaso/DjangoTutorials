from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView
from .views import ProductIndexView, ProductShowView, ProductCreateView
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("show/", views.show, name="show"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),

    path("products/", ProductIndexView.as_view(), name="products_index"),
    path("products/create/", ProductCreateView.as_view(), name="products_create"),
    path("products/<int:id>/", ProductShowView.as_view(), name="products_show"),
]
