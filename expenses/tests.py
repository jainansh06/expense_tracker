from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Category, Expense
from decimal import Decimal

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Food", color="#ff0000")
        self.assertEqual(category.name, "Food")
        self.assertEqual(str(category), "Food")

class ExpenseAPITest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Food")
        
    def test_create_expense(self):
        url = reverse('expense-list')  
        data = {
            'description': 'Lunch',
            'amount': 15.50,
            'category': self.category.id,
            'date': '2023-12-01'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)