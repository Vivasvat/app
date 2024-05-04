from django.urls import path
from main import views

app_name='main'

urlpatterns=[
    path("", views.index, name='index'),
    #path("next_page/", views.next_page, name='next_page'),
    path("create/", views.create, name='create'),
    path("edit/<int:id>/", views.edit, name='edit'),
    path("delete/<int:id>/", views.delete, name='delete')
]