from unittest import TestCase
from Receitas.sources.pagination import create_pagination_range

class PaginationTest(TestCase):

    def test_create_pagination_range_returns_a_pagination_range(self):

        pagination = create_pagination_range(
            page_range=list(range(1, 21)),
            pages=4,
            current_page=1
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_midle_page(self):

        pagination = create_pagination_range(
            page_range=list(range(1, 21)),
            pages=4,
            current_page=2
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = create_pagination_range(
            page_range=list(range(1, 21)),
            pages=4,
            current_page=3
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)
    
    def test_make_sure_midle_ranges_are_correct(self):

        pagination = create_pagination_range(
            page_range=list(range(1, 21)),
            pages=4,
            current_page=10
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        pagination = create_pagination_range(
            page_range=list(range(1, 21)),
            pages=4,
            current_page=11
        )['pagination']
        self.assertEqual([10, 11, 12, 13], pagination)
    
    def test_make_pagination_range_is_static_when_last_page_is_next(self):

        pagination = create_pagination_range(
            page_range=list(range(1, 21)),
            pages=4,
            current_page=18
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = create_pagination_range(
            page_range=list(range(1, 21)),
            pages=4,
            current_page=19
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
