from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator


class Category(models.Model):
    """
    Model for the product categories. The same as Boutique Ado Walkthrough.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for the products
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=254,
        unique=True,
        help_text='Full name including color if applicable.'
        )
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    weight_in_grams = models.IntegerField(
        null=True,
        blank=True,
        help_text='In grams. No decimals.'
        )
    price = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))])
    description = models.TextField()
    origin = models.CharField(max_length=254, null=True, blank=True)
    document_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        help_text='URL to manual or other file from manufacturer'
        )
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    """
    Model for keeping track of the quantity in stock
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
