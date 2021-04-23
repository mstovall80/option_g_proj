from django.urls import path
from .import views


urlpatterns= [
    path("", views.index),
    path('register', views.register),
    path("login", views.login),
    # path("user", views.User),
    path("main", views.main),
    path("quotes_list", views.quotes_list),
    path("add_quote", views.add_quote),
    path("user_quotes", views.user_quotes),
    path("edit_account", views.edit_account),
    path("logout", views.logout),
    path("delete_user", views.delete_user)
]

