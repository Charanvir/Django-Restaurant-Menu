from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


# ListView is better to pages which will have lots of data
# Variables need specific names
class MenuList(generic.ListView):
    # variable which will store the list of data
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self):
        context = {}
        context["meals"] = MEAL_TYPE
        return context


# DetailView is better for individual item views
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
