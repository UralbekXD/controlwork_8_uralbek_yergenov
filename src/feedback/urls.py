from django.urls import path

from feedback.views.products import ProductListView
from feedback.views.products import ProductDetailView
from feedback.views.products import ProductAddView
from feedback.views.products import ProductEditView
from feedback.views.products import ProductDeleteView

from feedback.views.reviews import ReviewAddView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductAddView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('product/<int:pk>/review/add', ReviewAddView.as_view(), name='review_add')

]