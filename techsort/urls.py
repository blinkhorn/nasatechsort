from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PrimaryTechList.as_view(), name='primarytech_list'),
    path('view/<int:pk>', views.PrimaryTechView.as_view(), name='primarytech_view'),
    path('new', views.PrimaryTechCreate.as_view(), name='primarytech_new'),
    path('view/<int:pk>', views.PrimaryTechView.as_view(), name='primarytech_view'),
    path('edit/<int:pk>', views.PrimaryTechUpdate.as_view(), name='primarytech_edit'),
    path('delete/<int:pk>', views.PrimaryTechDelete.as_view(), name='primarytech_delete'),
]