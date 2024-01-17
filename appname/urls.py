from django.urls import path
from . import views  # from(.)->current directory


app_name = "appname"  # so we can identify the template belong to this app as one project can have many apps
urlpatterns = [
    # path("", views.hello, name="hello"),
    path("", views.hello.as_view(), name="hello"),
    # path("<int:id>/", views.detail, name="detail"),
    path("<int:pk>/", views.detail.as_view(), name="detail"),
    # path("add", views.add_items, name="add_items"),
    path("add", views.add_items.as_view(), name="add_items"),
    path("update/<int:id>/", views.update_items, name="up_items"),
    path("delete/<int:id>/", views.delete_items, name="del_items"),
]
