from django.urls import path

from . import views


urlpatterns = [
    path('', views.asset_list_view),
    path('add/', views.asset_add_view),
    path('<str:pk>/', views.asset_details_view),
]
