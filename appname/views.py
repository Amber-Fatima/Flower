from django.shortcuts import render, redirect

from django.template import loader
from .models import Item
from .form_model import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
# it take request from user and respond to it


# def hello(request):
#     item = Item.objects.all()


#     context = {
#         "item": item,
#     }
#     return render(request, "appname/index.html", context)


# CLASS REPRESENTATION OF HELLO FUNCTION
class hello(ListView):
    model = Item
    template_name = "appname/index.html"
    context_object_name = "item"


# def detail(request, id=None):
#     item = Item.objects.get(pk=id)

#     context = {
#         "item": item,
#     }
#     return render(request, "appname/detail.html", context)


# CLASS REPRESENTATION OF DETAIL FUNCTION
class detail(DetailView):
    model = Item
    template_name = "appname/detail.html"
    context_object_name = "item"


# def add_items(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         # Set the user_name field to the currently logged-in user
#         form.instance.user_name = request.user
#         form.save()
#         return redirect("appname:hello")
#     context = {
#         "form": form,
#     }
#     return render(request, "appname/form_model.html", context)


class add_items(CreateView):
    model = Item
    fields = ["name", "item_desc", "price", "image"]
    template_name = "appname/form_model.html"

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_items(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect("appname:hello")
    context = {
        "form": form,
        "item": item,
    }
    return render(request, "appname/form_model.html", context)


def delete_items(request, id):
    item = Item.objects.filter(pk=id)
    if request.method == "POST":
        item.delete()
        return redirect("appname:hello")
    context = {
        "item": item,
    }
    return render(request, "appname/del_form.html", context)
