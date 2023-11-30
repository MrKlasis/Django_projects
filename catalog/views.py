from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Category, Product, Version
from catalog.services import get_object_list


class UserHasPermissionMixin:
    def has_permission(self):
        # Проверяем, является ли пользователь владельцем объекта, если да, то разрешаем операцию
        if self.model.objects.get(pk=self.kwargs.get('pk')).author == self.request.user:
            return True
        # если не является, то следуем ограничениям прав permission_required
        return super().has_permission()


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров',
    }

    def get_queryset(self):
        # возвращаем кэшированный queryset, который присвоится к object_list
        return get_object_list(self.model)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserHasPermissionMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        print(self.object.author)
        print(self.request.user)
        print(self.object.author != self.request.user)
        if self.object.author != self.request.user:
            self.form_class = ModeratorProductForm
        return self.form_class

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.model.author == self.request.user:
            VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
            if self.request.method == 'POST':
                context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
            else:
                context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, UserHasPermissionMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:category')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Все товары категории: {category_item.name}'

        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['product_pk'] = product_item.pk,
        context_data['title'] = f'{product_item.name}'

        return context_data


@login_required
@permission_required('catalog.set_publication')
def publication(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cat_pk = product.category.pk
    if product.publication:
        product.publication = False
    else:
        product.publication = True
    product.save()
    return redirect(reverse('catalog:product_list', kwargs={'pk': cat_pk}))


@login_required
def contacts(request):
    context = {
        'title': 'Контакты '
    }
    return render(request, 'catalog/contacts.html', context)
