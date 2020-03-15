from orders.models import User, Product, Order, Comment
from orders.serializers import UserSerializer, ProductSerializer, OrderSerializer, CommentSerializer, SingleOrderSerializer
from rest_framework import viewsets, generics, filters
from rest_framework.pagination import CursorPagination, PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    serializer_class = UserSerializer


class PageNumberSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = '10'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    serializer_class = ProductSerializer
    pagination_class = PageNumberSetPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer = OrderSerializer(queryset, many=True)
    serializer_class = OrderSerializer

class SingleOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer = SingleOrderSerializer(queryset, many=True)
    serializer_class = SingleOrderSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer = CommentSerializer(queryset, many=True)
    serializer_class = CommentSerializer
