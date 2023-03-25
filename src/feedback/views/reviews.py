from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from feedback.models import Review, Product
from feedback.forms import ReviewForm


class ReviewAddView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'feedback/products/product_detail.html'

    def form_valid(self, form):
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.product.pk})


