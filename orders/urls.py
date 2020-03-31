from django.conf.urls import url
from django.urls import path, include
from orders import views
from orders.views import user_login, LoginView
from orders.viewsets import UserViewSet, ProductViewSet, OrderViewSet, CommentViewSet
from rest_framework import routers
from django.contrib.auth import views as auth_views
from orders.views import schema_view

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'products', ProductViewSet, 'products')
router.register(r'order', OrderViewSet, 'order')
router.register(r'comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', views.index),
    path('chat', views.chat),
    path('<str:room_name>', views.room, name='room'),
    path('todos', views.todos),
    path('news', views.news),
    path('about', views.about),


    path('product_detail/<int:pk>/', views.product_detail),
    path('orders_list', views.orders_list_page, name='orders'),
    path('orders_list/create_order', views.order_page, name='order_page'),
    path('orders_list/single_order/<int:pk>/', views.single_order),

    url(r'^login', auth_views.LoginView.as_view(), {
        'template_name': 'login.html'}, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('api/', include(router.urls)),
    path('api/docs', schema_view),

]
