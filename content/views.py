from django.views.generic import DetailView, ListView

from content.models import Category, Subcategory, CategoryItem


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'objects'
    queryset = Category.objects.all()


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'caregory_detail.html'


class SubcategoryDetailView(DetailView):
    model = Subcategory
    template_name = 'subcategory_detail.html'


class ItemDetailView(DetailView):
    model = CategoryItem
    template_name = 'item_detail.html'
