# from django.contrib import admin
# from django.urls import path
# from website.api import views
# from rest_framework.authtoken import views as drf_views
# urlpatterns = [
#     # API endpoints
#     path('token/', views.obtain_auth_token, name = 'api-token-auth'),
#     path("add-product/", views.add_product, name="add_product"),
#     path('products/', views.get_products, name='get_products'),
#     path("update-product/<int:pk>/", views.update_product, name="update_product"),
#     path("delete-product/<int:pk>/", views.delete_product, name="delete_product"),
# ]


from django.contrib import admin
from django.urls import path
from website.api import views as api_views   # your custom API views
from rest_framework.authtoken.views import obtain_auth_token  # DRF's token view

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Authentication
    path('token/', obtain_auth_token, name='api_token_auth'),

    # API endpoints
    path("add-product/", api_views.add_product, name="add_product"),
    path("products/", api_views.get_products, name="get_products"),
    path("update-product/<int:pk>/", api_views.update_product, name="update_product"),
    path("delete-product/<int:pk>/", api_views.delete_product, name="delete_product"),
]
