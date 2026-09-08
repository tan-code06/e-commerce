# Ecom Project (Django + your Asbab frontend)

Your friend's static HTML template is now a working Django project. CSS, JS,
fonts, and theme images are wired up through Django's static file system, and
the **Shop** and **Product Details** pages pull real products from the
database instead of hardcoded HTML.

## What was done

- Created a Django project `ecom_project` with one app: `shop`.
- Copied `css/`, `js/`, `fonts/`, `images/`, `style.css` into `static/`.
- Converted all 8 pages (`index`, `product-grid`, `product-details`, `cart`,
  `checkout`, `wishlist`, `login`, `contact`) into Django templates under
  `templates/shop/`:
  - Every `href="css/..."`, `src="js/..."`, `src="images/..."` was replaced
    with `{% static '...' %}` tags.
  - Every internal link (`index.html`, `cart.html`, etc.) was replaced with
    named `{% url 'shop:...' %}` tags, so links won't break if routes change.
- Added a `Product` model (`shop/models.py`) with name, slug, price,
  old_price, description, image, stock.
- `product_grid.html` and `product_details.html` now loop over real
  `Product` objects from the database (`{% for product in products %}`)
  instead of 12 copy-pasted HTML cards.
- `index.html`, `cart.html`, `checkout.html`, `wishlist.html`, `login.html`,
  `contact.html` are wired up (routes + static files work) but still show
  the original static demo content — you picked "dynamic grid/details
  pages" as the scope, so cart/checkout logic isn't built yet.
- Added a `seed_products` management command that creates 12 demo products
  using the template's own `images/product/1.jpg`–`12.jpg`, so the site has
  something to show immediately.

## Setup

```bash
# 1. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations (creates db.sqlite3 and the products table)
python manage.py migrate

# 4. Seed demo products (uses the template's own images)
python manage.py seed_products

# 5. Create an admin login so you can add/edit products yourself
python manage.py createsuperuser

# 6. Run the dev server
python manage.py runserver
```

Then visit:
- http://127.0.0.1:8000/ — homepage
- http://127.0.0.1:8000/shop/ — product grid (from the database)
- http://127.0.0.1:8000/admin/ — add, edit, or delete products
- Click any product on the grid to see its dynamic details page.

## Adding real products

Go to `/admin/`, log in with the superuser you created, click **Products →
Add product**, and upload a real image. It'll show up on `/shop/`
immediately — no template edits needed.

## Project layout

```
ecom_project/
  manage.py
  ecom_project/        settings.py, urls.py, wsgi.py, asgi.py
  shop/                models.py, views.py, urls.py, admin.py
    management/commands/seed_products.py
  templates/shop/       all 8 converted pages
  static/               css/ js/ fonts/ images/ style.css (theme assets)
  media/products/       uploaded/seeded product images (created at runtime)
```

## Next steps you may want

- Extract the shared header/nav/footer into a `base.html` with
  `{% block content %}` so you're not editing 8 files for one nav change.
- Add real cart logic (Django sessions or a `Cart`/`CartItem` model) to
  `cart.html` and `checkout.html`.
- Hook up `login.html` to Django's built-in auth (`django.contrib.auth`).
- Deploy: switch `DEBUG = False`, set `ALLOWED_HOSTS`, and serve static
  files with `whitenoise` or nginx (Django doesn't serve static files
  itself in production).
