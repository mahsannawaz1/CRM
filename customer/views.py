from django.shortcuts import render, redirect
from .forms import productCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


@login_required
def addProduct(request):
    form = productCreationForm()
    if request.method == 'POST':
        form = productCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')

    context = {
        'form': form
    }
    return render(request, 'customer/add_product.html', context)


def listProducts(request):
    products = Product.objects.all().values()
    context = {
        'products': list(products)
    }

    return render(request, 'customer/list_products.html', context)


@login_required
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = productCreationForm(instance=product)
    if request.method == 'POST':
        form = productCreationForm(
            request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')

    context = {
        'form': form
    }

    return render(request, 'customer/update_product.html', context)


@login_required
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    context = {
        'product': product
    }
    return render(request, 'customer/delete_product.html', context)


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'customer/create_order.html'
    context_object_name = 'form'
    fields = ['order_status', 'discount', 'product', 'description']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Order
    template_name = 'customer/update_order.html'
    context_object_name = 'form'
    fields = ['order_status', 'discount', 'product', 'description']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        if order.customer == self.request.user:
            return True
        return False


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Order
    template_name = 'customer/update_order.html'
    context_object_name = 'order'

    def test_func(self):
        order = self.get_object()
        if order.customer == self.request.user:
            return True
        return False


class ListOrdersView(ListView):
    model = Order
    template_name = 'customer/order_list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']
