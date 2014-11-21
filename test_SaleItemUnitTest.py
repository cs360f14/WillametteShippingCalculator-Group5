#!/usr/bin/python3

################################
# File Name:	test_SaleItemUnitTest.py
# Author:		Chadd Williams - Huyen Tran
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Unittest for SaleItem
################################

# python3 -m unittest test_SaleItemUnitTest -v

import unittest
from SaleItem import SaleItem

class TestSaleItem(unittest.TestCase):
	
	
	def setUp(self):
		""" the text fixture, necessary setup for the tests to run
		"""
		self.theSaleItem = SaleItem(['10', '2', 'TestItem'])
		
		
	def tearDown(self):
		""" nothing to tear down here
		If your test created a database or built a network connection
		you might delete the database or close the network connection
		here. You might also close files you opened, close your
		TK windows if this is GUI program, or kill threads if this is
		a multithreaded application
		"""
		pass # nothing to do


	def test_GetCost(self):
		self.assertEqual(self.theSaleItem.getCost(), '10')
	
	def test_GetWeight(self):
		self.assertEqual(self.theSaleItem.getWeight(), '10')
	
	def test_GetTitle(self):
		self.assertEqual(self.theSaleItem.getTitle(), 'TestItem')

	def test_GetFreeShipping(self):
		
		# the default item in setUp() does not have free
		# shipping
		
		self.assertEqual(self.theSaleItem.getFreeShipping(), False)
		
		
		itemWithFreeShipping = SaleItem(['10', '2', 'FSTestItem', 'FS'])
		self.assertEqual(itemWithFreeShipping.getFreeShipping(), True)
	
	def test_GetDetailsAsString(self):
		self.assertEqual(self.theSaleItem.getDetailsAsString(), 'TestItem $10')
