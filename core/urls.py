from django.urls import path
from . import views

app_name = 'cliente'


urlpatterns = [
    path('list/', views.ListClientes.as_view(), name='list'),
    path('created/', views.CreateCliente.as_view(), name='created'),
    path('update/<int:pk>/', views.UpdateCliente.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete')
]
