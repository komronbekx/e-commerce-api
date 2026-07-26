from apps.products.views.product import ProductView, ProductDetailView
from apps.products.views.product_image import ProductImageView, ProductImageDetailView
from django.urls import path
from apps.products.views import CategoryDetailView, CategoryView

urlpatterns = [
    path("categories/", CategoryView.as_view(), name="categories"),
    path(
        "categories/<uuid:category_id>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path("products/", ProductView.as_view(), name="products"),
    path(
        "products/<uuid:product_id>/", ProductDetailView.as_view(), name="product-detail"
    ),
    path(
        "products/<uuid:product_id>/images/",
        ProductImageView.as_view(),
        name="product-images",
    ),
    path(
        "products/<uuid:product_id>/images/<uuid:image_id>/",
        ProductImageDetailView.as_view(),
        name="product-image-detail",
    ),
]
