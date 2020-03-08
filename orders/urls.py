from django.conf.urls import url
from django.urls import path, include
from orders import views
from orders.views import user_login, LoginView
from orders.viewsets import UserViewSet, ProductViewSet, OrderViewSet, CommentViewSet

from rest_framework import routers

from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'products', ProductViewSet, 'products')
router.register(r'order', OrderViewSet, 'order')
router.register(r'comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', views.index),
    path('orders_list', views.orders_list_page, name='orders'),
    path('orders_list/order', views.order_page, name='order_page'),
    url(r'^login', auth_views.LoginView.as_view(), {
        'template_name': 'login.html'}, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('api/', include(router.urls)),
]
