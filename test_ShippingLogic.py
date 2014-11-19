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


class TestShippingLogic:
	def setUp (self):
		self.theShippingLogic = ShippingLogic ()
		
	def test_calcWeightForCost (self):
		testBasket = basket ()
		testItemStore = itemStore ('dataFiles/normalSales.csv')
		testSaleItem = SaleItem (10, 2, 'Test Item', False, 1)
		testBasket.addItem  
		
		
