from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='subcategories')

    def __str__(self):
        return self.name


class CategoryItem(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True,
                                    on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name
