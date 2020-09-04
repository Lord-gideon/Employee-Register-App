from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.employee_form, name='employee_create'), #post req for creating 
    path('<int:id>/',views.employee_form, name="employee_update"), #for get and post for update
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/',views.employee_list, name='employee_list'), #get req to retrieve and display a list of entry from data base
    
]