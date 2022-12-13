from django.urls import path
from . import views


urlpatterns = [
    path('', views.branch_list_view),
    path('<int:pk>', views.brach_details_view),
    path('', views.add_branch_view),
]
