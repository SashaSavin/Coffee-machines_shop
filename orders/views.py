from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from orders.forms import LoginForm

from django.views.decorators.csrf import csrf_exempt

from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from orders.models import Order, User

from django.contrib.auth.decorators import login_required
from orders.forms import OrderForm


def index(request):
    return render(request, "index.html")


@login_required
def orders_list_page(request):
    data = {'Order': Order.objects.all(
    ), 'User': User.objects.filter(user_type='MN')}

    return render(request, "order_list.html", context=data)


@login_required
def single_order(request):
     return render(request, "single_order.html")


@login_required
def order_page(request):
    if request.method == "POST":
        form = OrderForm(request.POST )
        if form.is_valid():
            order = form.save(commit=False)

            order.save()
            return redirect("http://localhost:8000/orders_list")
    else:
        form = OrderForm()
    return render(request, "order.html",  {'form': form})


@csrf_exempt
def user_login(request):
    userform = LoginForm()
    if request.method == "POST":
        userform = LoginForm(request.POST)
        if userform.is_valid():
            return redirect('orders')
    return render(request, "registration/login.html", {"form": userform})


