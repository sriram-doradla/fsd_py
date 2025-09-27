from django.contrib import admin
from website import views
from django.urls import include, path
urlpatterns = [
    # these are web urls
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/',views.search, name='search'),

    path("api/", include("website.api.urls")),
    # API endpoints
    # path("add-product/", views.add_product, name="add_product"),
    # path('api/products/', views.get_products, name='get_products'),
    # path("update-product/<int:pk>/", views.update_product, name="update_product"),
    # path("delete-product/<int:pk>/", views.delete_product, name="delete_product"),
    # path("register/", views.register_user, name="register_user"),
]
