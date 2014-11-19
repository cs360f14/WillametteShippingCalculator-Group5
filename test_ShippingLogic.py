#!/usr/bin/python3

################################
# File Name:	test_ShippingLogic.py
# Author:		Kevin Jo
# Date:			10/30/2014
# Class:		CS 360
# Assignment:	Python Classes
# Purpose:		
################################

import unittest 
from ShippingLogic import *
from basket import *
from itemStore import *


class TestShippingLogic (unittest.TestCase):
	def setUp (self):
		self.theShippingLogic = ShippingLogic ()
		
	def test_calcCostForShippingByWeight (self):
		self.assertEqual (self.theShippingLogic.calcCostForShippingByWeight (.1), 6)
		self.assertEqual (self.theShippingLogic.calcCostForShippingByWeight (.9), 6)
		self.assertEqual (self.theShippingLogic.calcCostForShippingByWeight (1), 8)
		self.assertEqual (self.theShippingLogic.calcCostForShippingByWeight (4), 8)
		self.assertEqual (self.theShippingLogic.calcCostForShippingByWeight (5), 11)
		self.assertEqual (self.theShippingLogic.calcCostForShippingByWeight (10), 11)
		self.assertEqual (self.theShippingLogic.calcCostForShippingByWeight (101), 1)
		
