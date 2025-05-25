from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreate.as_view()),
    path('expenses/', views.ExpenseListCreate.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view()),
    path('stats/', views.expense_stats),
]