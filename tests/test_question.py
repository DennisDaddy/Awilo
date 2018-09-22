"""Impot python modules"""
import unittest
import json
import os
import sys
from app import *
sys.path.insert(0, os.path.abspath(".."))

class QuestionsTestCase(unittest.TestCase):
    def setUp(self):
		"""Define test variables and initialize the app."""
		self.app = create_app(config_name="testing")
		self.client = self.app.test_client

    def test_home(self):
		"""This method tests root endpoint"""
		tester = app.test_client(self)
		response = tester.get('/api/v1', content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Welcome to Stackoverflow-lite', response.data)