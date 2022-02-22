import unittest
import browser as main


class TestIteSpider(unittest.TestCase):
    def test_request(self):
        main.url = 'http://www.ite.edu.sg/'


if __name__ == '__main__':
    unittest.main()

