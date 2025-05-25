from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

@api_view(['GET'])
def expense_stats(request):
    total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    expense_count = Expense.objects.count()
    
    categories_data = []
    for category in Category.objects.all():
        cat_total = Expense.objects.filter(category=category).aggregate(Sum('amount'))['amount__sum'] or 0
        if cat_total > 0:
            categories_data.append({
                'name': category.name,
                'total': float(cat_total),
                'color': category.color
            })
    
    return Response({
        'total_expenses': float(total_expenses),
        'expense_count': expense_count,
        'categories': categories_data
    })