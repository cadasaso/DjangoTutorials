from django.http import HttpResponse
from django.views import View
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product,Comment
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404

def show(request):
    products = Product.objects.all()
    return render(request, "show.html", {"products": products})

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context
    


class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.objects.all()
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError
        except ValueError:
            return HttpResponseRedirect(reverse("home"))

        product = get_object_or_404(Product, pk=product_id)

        viewData = {}
        viewData["title"] = product.name + " - Online Store"
        viewData["subtitle"] = product.name + " - Product information"
        viewData["product"] = product
        viewData["comments"] = product.comments.all()
        return render(request, self.template_name, viewData)




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price"]

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
           form.save()  # <-- GUARDA en la BD
           return HttpResponseRedirect("/products/")  # o reverse(...) si usas nombres

        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
