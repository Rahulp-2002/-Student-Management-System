
from django.contrib import admin
from django.urls import path
from B_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('RP', views.my_page),
    path("Add", views.add_page),
    path("Edit/<int:id>" ,views.edit_page),
    path("Details/<int:id>" ,views.details_page),
    path("Delete/<int:id>" , views.delete_page),
    path("register", views.register_page),
    path("login", views.login_page),
    path("logout", views.logout_page),

]
