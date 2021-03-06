from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.get_dashboard_mygigs, name="dashboard"),
    path("orders/", views.get_dashboard_orders, name="dashboard-orders"),
    path("profile-edit/", views.get_dashboard_profile_edit, name="dashboard-profile-edit"),
    path("accept_orders/", views.set_order_status, name="set_status"),
    path("comments/", views.get_dashboard_comments, name="dashboard-comments"),
    path("myorders/", views.get_dashboard_myorders, name="dashboard-myorders"),
    # path("messages/", views.register, name="dashboard-messages"),
    # path("wallet/", views.register, name="dashboard-wallet"),
    # path("settings/", views.register, name="dashboard-settings"),
]
