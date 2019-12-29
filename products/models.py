from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 80, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key= True)
    title = models.CharField('Name', max_length= 255, blank=False, null=False)
    category_id = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['title']

    def __str__(self):
        return self.title