from django.urls import path
from . import views


urlpatterns = [

    path('', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('subcategory/<int:pk>', views.SubcategoryDetailView.as_view(), name='subcategory-detail'),
    path('categoryitem/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
]