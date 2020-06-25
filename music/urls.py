
from django.urls import include, path
from .views import DescCreate,DescUpdate,DescDelete
from . import views
from django.contrib import admin


urlpatterns = [
    path('music/destination_form/', DescCreate.as_view(),name='create-form' ),
    path('music/<pk>/update_form' ,DescUpdate.as_view(), name='update-form'),
    path('music/<pk>/destination_confirm_delete', DescDelete.as_view(), name='delete-form'),
    path('', views.index, name='index')

]
