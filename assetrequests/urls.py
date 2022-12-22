from django.urls import path

from . import views


urlpatterns = [
    path('', views.asset_request_list_view),
    path('<int:pk>/', views.asset_request_details_view),
    path('add/', views.asset_request_add_view),
    path('delete/<int:pk>/', views.asset_request_remove_view),
    path('update/<int:pk>/',views.asset_update_Status),
]
