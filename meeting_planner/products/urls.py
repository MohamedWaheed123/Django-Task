from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('products', views.products_list, name="products"),
    path('register', views.register, name="register")

]