from typing import Any

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView


class Register(CreateView):
    form_class: type[UserCreationForm] = UserCreationForm
    success_url: str | Any | None = reverse_lazy('login')
    template_name: str = 'cadastro.html'

    def form_valid(
        self, form: UserCreationForm, *args, **kwargs
    ) -> HttpResponse:
        messages.success(self.request, 'Cadastro realizado com sucesso!')
        return super(Register, self).form_valid(form, *args, **kwargs)
