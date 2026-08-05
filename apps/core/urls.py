from django.urls import include, path

urlpatterns = [
    path("", include("apps.products.urls")),
    path("", include("apps.auth.urls")),
    path("", include("apps.cart.urls")),
    path("", include("apps.orders.urls")),
    # path("payments/", include("apps.payments.urls")),
]
