from django.urls import include, path

urlpatterns = [
    # path("categories/", include("apps.products.urls.category_urls")),
    path("categories/", include("apps.products.urls")),
    # path("orders/", include("apps.orders.urls")),
    # path("payments/", include("apps.payments.urls")),
]
