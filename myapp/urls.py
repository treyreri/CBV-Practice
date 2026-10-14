from django.urls import path
from .views import(CategoryListCreateAPIView, CategoryDetailAPIView, ProductDetailAPIView, ProductListCreateAPIView)
urlpatterns = [
    path('categories/' , CategoryListCreateAPIView.as_view(), name = 'category-list-create') ,
    path('categories/<int:pk>/', CategoryListCreateAPIView.as_view(), name = 'product-list-create') ,
    path('products/' , ProductListCreateAPIView.as_view() , name = 'product-list-create') ,
    path('products/<int:pk>/' , ProductDetailAPIView.as_view() , name = 'product-detail') ,
]