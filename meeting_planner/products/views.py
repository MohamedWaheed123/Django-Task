from django.shortcuts import render, get_object_or_404,redirect
from .models import Product, User
from .forms import RegisterForm


def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/detail.html", {"product": product})


def products_list(request):
    return render(request, "products/products_list.html",
            {"products": Product.objects.all()})




def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = RegisterForm()
    return render(request, "products/register.html", {"form": form})

