
from django.urls import path

from bikes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cyklos/', views.CykloListView.as_view(), name='cyklo_list'),
    path('cyklos/<int:pk>/', views.CykloDetailView.as_view(), name='cyklo-detail'),
    path('cyklos/types/<str:type_bike_type>/', views.CykloListView.as_view(), name='cyklo_type'),
    path('topten', views.topten, name='topten'),
    path('cyklo/create/', views.CykloCreateView.as_view(), name='cyklo-create'),
    path('cyklo/<int:pk>/update/', views.CykloUpdateView.as_view(), name='cyklo-update'),
    path('cyklo/<int:pk>/delete/', views.CykloDeleteView.as_view(), name='cyklo-delete'),
    path('prodejny', views.prodejny, name='prodejny'),

]