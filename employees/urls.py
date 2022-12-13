from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee_view),
    path('<int:pk>/', views.employee_details_view),
    path('add/', views.add_employee_view)
]
