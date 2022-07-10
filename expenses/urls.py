from django.urls import include, path
from . import views

urlpatterns = [
    path('create/', views.ExpenseCreateView.as_view(), name='create_expense'),
    path('list/', views.ExpenseListView.as_view(), name='list_expense')
]