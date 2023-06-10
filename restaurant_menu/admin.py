from django.contrib import admin

from restaurant_menu.models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "meal_type", "price", "status")
    list_filter = ("status", "price", "meal_type")
    search_fields = ("meal", "description")


# Coupling the database class with the admin class
admin.site.register(Item, MenuItemAdmin)
