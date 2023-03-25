from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from feedback.models import Product
from feedback.forms import ProductForm, ReviewForm


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'feedback/index.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetailView(DetailView):
    model = Product
    template_name = 'feedback/products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = self.object
        context['reviews'] = product.product_review.all()
        context['review_form'] = ReviewForm()
        return context


class ProductAddView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'feedback/products/product_create.html'
    success_url = reverse_lazy('products')


class ProductEditView(UpdateView):
    model = Product
    template_name = 'feedback/products/product_update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products')
