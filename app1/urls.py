from django.urls import path
from .import views

app_name="app1"


urlpatterns = [
    path('', views.home,name='home'),
    path('details/<int:id>/',views.detail,name="detail"),
    path('addcolleges/', views.add_colleges, name="add_colleges"),
    path('editcolleges/<int:id>/', views.edit_colleges, name="edit_colleges"),
    path('deletecolleges/<int:id>/', views.delete_colleges, name="delete_college")
]
