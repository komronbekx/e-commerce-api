from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from apps.orders.models import Order, OrderItem


class OrderItemInline(TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ("id", "user", "status", "total_price", "created_at")
    list_filter = ("status",)
    search_fields = ("user__email", "id")
    inlines = [OrderItemInline]
