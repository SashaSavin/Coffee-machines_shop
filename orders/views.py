from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from rest_framework_swagger.views import get_swagger_view
from orders.forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from orders.models import Order, User, Product, Comment
from django.contrib.auth.decorators import login_required
from orders.forms import OrderForm, CommentForm, ProductForm
import logging

logger = logging.getLogger(__name__)

schema_view = get_swagger_view(title='Orders application API')


def index(request):
    form = ProductForm()
    return render(request, "index.html", context={'product': form})


@login_required
def chat(request):
    return render(request, "chat.html")

@login_required
def todos(request):
    return render(request, "todo.html")

@login_required
def news(request):
    return render(request, "news.html")


def about(request):
    return render(request, "about.html")


@login_required
def orders_list_page(request):
    data = {'Order': Order.objects.all(),
            'User': User.objects.filter(user_type='MN')}
    return render(request, "order_list.html", context=data)


@login_required
def single_order(request, pk):
    data = Order.objects.get(id=pk)
    form = OrderForm()
    return render(request, "single_order.html", context={'data': data, 'form': form})


@login_required
def product_detail(request, pk):
    data = Product.objects.get(id=pk)
    comment = Comment.objects.get()
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.data = data
            new_comment.save()
        else:
            comment_form = CommentForm()
    return render(request, "product_detail.html", context={'data': data, 'comment_form': comment_form, 'cmt': comment})


@login_required
def order_page(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            order.save()
            return redirect("http://localhost:8000/orders_list")
    else:
        form = OrderForm()
    return render(request, "order.html", {'form': form})


@csrf_exempt
def user_login(request):
    userform = LoginForm()
    if request.method == "POST":
        userform = LoginForm(request.POST)
        if userform.is_valid():
            return redirect('orders')
    return render(request, "registration/login.html", {"form": userform})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })