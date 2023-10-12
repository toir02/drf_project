from rest_framework.pagination import PageNumberPagination


class EducationPaginator(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100
