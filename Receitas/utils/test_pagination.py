from unittest import TestCase
from Receitas.sources.pagination import create_pagination_range

class PaginationTest(TestCase):

    def test_create_pagination_range_returns_a_pagination_range(self):

        pagination = create_pagination_range(
            page_range=list(range(1, 21)),
            pages=4,
            current_page=1
        )
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_midle_page(self):
        ...
