import shutil
from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from shop.models import Product

# (name, price, old_price, source image filename under static/images/product/)
DEMO_PRODUCTS = [
    ("Largest Water Pot", 25.90, 30.30, "1.jpg"),
    ("Ceramic Vase Set", 18.50, None, "2.jpg"),
    ("Classic Wall Clock", 42.00, 49.99, "3.jpg"),
    ("Wooden Table Lamp", 33.75, None, "4.jpg"),
    ("Cotton Throw Pillow", 12.20, 15.00, "5.jpg"),
    ("Rustic Photo Frame", 9.99, None, "6.jpg"),
    ("Woven Storage Basket", 27.40, 32.00, "7.jpg"),
    ("Handmade Coffee Mug", 8.50, None, "8.jpg"),
    ("Bamboo Cutting Board", 15.60, 19.90, "9.jpg"),
    ("Glass Flower Vase", 21.30, None, "10.jpg"),
    ("Linen Table Runner", 14.75, 17.50, "11.jpg"),
    ("Decorative Candle Set", 11.40, None, "12.jpg"),
]


class Command(BaseCommand):
    help = "Seeds the database with demo products using the template's own product images."

    def handle(self, *args, **options):
        source_dir = Path(settings.BASE_DIR) / 'static' / 'images' / 'product'
        created_count = 0

        for name, price, old_price, filename in DEMO_PRODUCTS:
            slug = slugify(name)
            if Product.objects.filter(slug=slug).exists():
                self.stdout.write(f"Skipping '{name}' (already exists)")
                continue

            source_path = source_dir / filename
            if not source_path.exists():
                self.stdout.write(self.style.WARNING(
                    f"Image not found for '{name}': {source_path}"
                ))
                continue

            product = Product(
                name=name,
                slug=slug,
                description=(
                    f"{name} — a placeholder product description seeded from the "
                    "original frontend template. Edit this in the Django admin."
                ),
                price=price,
                old_price=old_price,
                stock=25,
            )
            with open(source_path, 'rb') as f:
                product.image.save(filename, File(f), save=False)
            product.save()
            created_count += 1
            self.stdout.write(self.style.SUCCESS(f"Created '{name}'"))

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created_count} product(s) created."
        ))
