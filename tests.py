import unittest
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import app as app_module

if os.path.exists("env.py"):
    import env

app = app_module.app

# Setting up test DB on Mongo and switching CSRF checks off
app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)
app_module.mongo = mongo


class AppTestCase(unittest.TestCase):
    """TestCase Class"""
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        """Test Home page load response and headers"""
        res = self.client.get('/')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Welcome to the Kitchen Craft website!' in data

    def test_recipes(self):
        """Test Recipes Page load response and headers"""
        res = self.client.get('/recipes')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Search our recipes' in data

    def test_products(self):
        """Test Products Page load response and headers"""
        res = self.client.get('/products')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Products - Kitchen Craft Certified' in data

    def test_cuisines(self):
        """Test Cuisines Page load response and headers"""
        res = self.client.get('/cuisines/')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Read about all the cuisines of the world below' in data

    def test_register(self):
        """Test Register Page load response and headers"""
        res = self.client.get('/register')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Register' in data

    def test_login(self):
        """Test Log In Page load response and headers"""
        res = self.client.get('/login')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Log In' in data

    def test_register_functionality(self):
        """Test Register functionality"""
        res = self.client.post('/register', data=dict(
            username='testcase1',
            fname='Test',
            lname='Case',
            password='TestCase1!',
            pconfirm='TestCase1!',
            email='testcase@testingkitchencraft.com'
        ))
        data = res.data.decode('utf-8')
        assert 'testcase' in data

if __name__ == '__main__':
    unittest.main()
