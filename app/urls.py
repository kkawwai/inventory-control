from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_view'),
    path('list_warehouse/', views.List_WarehouseView.as_view(), name='list_warehouse'),
    path('list_one/', views.List_OneView.as_view(), name='list_one'),
    path('list_two/', views.List_TwoView.as_view(), name='list_two'),
    path('list_three/', views.List_ThreeView.as_view(), name='list_three'),
    path('list_central/', views.List_CentralView.as_view(), name='list_central'),
    path('search/', views.List_Search_View.as_view(), name='search'),
    path('more/', views.More_Deli, name='more'),
    path('send/', views.Send_Deli, name='send'),
    path('create/', views.CreateView, name='create'),
    path('liquidation_one/', views.Liquidation_one_View, name='liquidation_one'),
    path('liquidation_two/', views.Liquidation_two_View, name='liquidation_two'),
    path('liquidation_three/', views.Liquidation_three_View, name='liquidation_three'),
    path('liquidation_central/', views.Liquidation_central_View, name='liquidation_central'),
]