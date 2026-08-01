from django.urls import include, path

urlpatterns = [
    # path("categories/", include("apps.products.urls.category_urls")),
    path("", include("apps.products.urls")),
    path("", include("apps.auth.urls")),
    # path("orders/", include("apps.orders.urls")),
    # path("payments/", include("apps.payments.urls")),
]
