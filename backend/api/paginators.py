from rest_framework.pagination import PageNumberPagination


class PageLimitPagination(PageNumberPagination):
    """
    Стандартный пагинатор для вывода запрошенного количества страниц.
    """
    page_size_query_param = 'limit'
