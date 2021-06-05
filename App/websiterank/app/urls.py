from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('templates/about', views.about, name='about'),
    path('templates/ranking',views.graph, name = 'graph'),
    path('templates/dbupdate',views.update_db, name = 'update_db'),
    path('templates/details',views.detail_data_view, name = 'detail_data_view'),
    path('templates/addUniversity',views.add_university, name = 'addUni'),
    path('templates/add_university',views.addUniversity, name = 'addUniversity'),
    path('templates/deleteUniversity',views.deleteUniversity, name = 'deleteUni'),
    path('templates/delete_university',views.delete_university, name = 'delete')
]


