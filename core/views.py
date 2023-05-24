from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm
from django.urls import reverse_lazy


class ListClientes(ListView):
    template_name = 'index.html'
    model = Cliente
    context_object_name = 'clientes'


class CreateCliente(CreateView):
    form_class = ClienteForm
    template_name = 'form.html'
    success_url = reverse_lazy('cliente:list')


class UpdateCliente(UpdateView):
    template_name = 'form.html'
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:list')


class DeleteView(DeleteView):
    model = Cliente
    template_name = 'confirm.html'
    success_url = reverse_lazy('cliente:list')
    context_object_name = 'cliente'
