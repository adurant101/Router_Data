import unittest
from router_parse import Router

class TestRouterData(unittest.TestCase):
    router = Router('screen_output.txt')
    # Expected value from testing
    search_expected = ['10.156.43.100/24', 'u/u', 'a-1g/a-full', 'Mgmt', 'Network']
    # Actual value returned
    search_actual = router.search_router_data('dp0p7s0')
    
    def test_router_data(self):
        # Test router search from actual data vs expected
        self.assertEqual(self.__class__.search_expected,
        self.__class__.search_actual, "Search value not equal")
