from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class WatchListPagination(PageNumberPagination):
    page_size = 5
    

    