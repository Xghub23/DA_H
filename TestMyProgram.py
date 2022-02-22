import unittest
import browser as main


class TestIteSpider(unittest.TestCase):
    def test_request(self):
        main.url = 'http://www.webcode.me'


if __name__ == '__main__':
    unittest.main()

