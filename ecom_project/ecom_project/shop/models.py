from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True,
        help_text="Optional. Set this to show a strikethrough 'was' price."
    )
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_details', args=[self.slug])
