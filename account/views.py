from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name: str = 'cadastro.html'

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Cadastro realizado com sucesso!')
        return super(Register, self).form_valid(form, *args, **kwargs)
