from django.shortcuts import render

# Create your views here.

from rest_framework.generics import( ListCreateAPIView, RetrieveUpdateAPIView )
from drf_yasg.utils import swagger_auto_schema
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(operation_summary="List categories" , responses={200 : CategorySerializer(many=True)})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="List categories" , responses={200 : CategorySerializer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CategoryDetailAPIView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(responses={200:CategorySerializer, 404: 'Not found'})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(request_body=CategorySerializer , responses= {200 : CategorySerializer, 400 : 'Validation error' , 404 : 'Not found' })
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(request_body=CategorySerializer , responses= {200 : CategorySerializer, 400 : 'Validation error' , 404 : 'Not found' })
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(responses={204 : 'Deleted' , 404 : 'Not found'})
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(responces = {200 : ProductSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ProductSerializer, responces = {201:ProductSerializer, 400:'Validation error'})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title' , 'description']
    ordering_fields = ['price' , 'created_at' , 'title']

#/api/products/?min_price=100 цена от 100
#/api/products/?max_price=500 цена до 500
#/api/products/?search=phone поиск по названию




class ProductDetailAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(responses={200:ProductSerializer, 404 : 'Not found'})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ProductSerializer, responses={200:ProductSerializer, 400:'Validation error' , 404:'Not found'})
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ProductSerializer, responses={200: ProductSerializer,400: 'Validation error',404: 'Not found',})
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(responses={204: 'Deleted', 404: 'Not found'} )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)





from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter
from .filters import ProductFilter