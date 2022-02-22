import unittest

import scrapy

from spiders import ite


class TestIteSpider(unittest.TestCase):
    def test_parse(self):
        result = ite.parse()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

