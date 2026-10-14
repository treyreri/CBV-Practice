from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


#Пагинация разделяет большой список товаров на страницы
#напимер
#/api/products/ — первая страница
#/api/products/?page=2 — вторая страница
#/api/products/?page_size=10 — запросить до 10 объектов на странице