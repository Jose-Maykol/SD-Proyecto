from django.urls import include, path
from . import views

urlpatterns = [
    path('create/', views.IncomeCreateView.as_view(), name='create_income'),
    path('list/', views.IncomeListView.as_view(), name='list_income')
]

