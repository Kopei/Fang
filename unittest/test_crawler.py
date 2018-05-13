#!coding:utf8
import unittest
from ..crawler import *


class TestCrawler(unittest.TestCase):
    def test_getAmountForSale(self):
        zoneID = '5011000016950'
        r = getErShouFang(zoneID)
        self.assertEqual(r, 3)

    # def test_sumresul2(self):
	# l = [2]
	# s = sum1(l)
    #     print('the sum2 is %s' %s)
	# self.assertEqual(s, 2)
    #
    # def test_listemelent(self):
    #     l = [1,232,424,223,2]
	# n = listelement(l)
	# print('the list num is %s' %n)
	# self.assertEqual(5, n)
    #
    # def test_findmax(self):
    #     l = [1,232,424,223,2]
	# n = findmax(l)
	# self.assertEqual(n,424)


if __name__ == '__main__':
    unittest.main()
