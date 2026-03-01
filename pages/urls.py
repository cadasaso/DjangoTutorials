from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView
from .views import ProductIndexView, ProductShowView, ProductCreateView,CartRemoveAllView,CartView,ImageViewFactory 
from . import views
from .utils import ImageLocalStorage


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("show/", views.show, name="show"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),

    path("products/", ProductIndexView.as_view(), name="products_index"),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path("products/create/", ProductCreateView.as_view(), name="products_create"),
    path("products/<int:id>/", ProductShowView.as_view(), name="products_show"),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
]
