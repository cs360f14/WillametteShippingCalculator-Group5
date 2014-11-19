#!/usr/bin/python3

################################
# File Name:	test_ShippingLogicUnitTest.py
# Author:		Kelsey Yamaguchi
# Date:			11/19/2014
# Class:		CS 360
# Assignment:   Willamette Shipping Calculator
# Purpose:		Test the Shipping Logic class
################################

# adapted from https://docs.python.org/3/library/unittest.html

# python3 -m unittest test_ShippingLogicUnitTest -v

import random
import unittest
from ShippingLogic import *
from basket import *
from SaleItem import *

"""
Unit testing for TicTacToe game functions
"""

class TestShippingLogic (unittest.TestCase):
	
	def setUp (self):
		
		"""
		The necessary set up for Shipping Logic
		"""
		
		self.theSetUp = ShippingLogic()
		
	def test_calcWeightForCost (self):
		
		"""
		Test to calculate weight for cost
		"""
		
		self.basket = Basket()
		self.details = [50, 50, "Book"]
		self.details1 = [60, 50, "Magazine"]
		
		saleItem = SaleItem(self.details)
		saleItem2 = SaleItem(self.details1)
		
		self.basket.addItem([1, saleItem])
		self.basket.addItem([1, saleItem2])
		
		self.assertEqual(self.theSetUp.calcWeightForCost(self.basket), 111)
		
		

def main ():
	unittest.main()
				
						
if __name__ == '__main__':
	unittest.main ()
