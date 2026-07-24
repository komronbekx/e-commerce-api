from django.urls import path

from apps.products.views import CategoryDetailView, CategoryView

urlpatterns = [
    path("", CategoryView.as_view(), name="categories"),
    path("<uuid:category_id>/", CategoryDetailView.as_view(), name="category-detail"),
]
