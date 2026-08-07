from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from apps.cart.models import Cart, CartItem


class CartItemInline(TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(ModelAdmin):
    list_display = ("user", "created_at", "updated_at")
    search_fields = ("user__email",)
    inlines = [CartItemInline]
