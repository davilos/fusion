from django.http.response import HttpResponse
from django.test import TestCase
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.dados: dict[str, str] = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem',
        }

    def test_form_valid(self) -> None:
        request: HttpResponse = self.client.post(
            reverse_lazy('index'), data=self.dados
        )

        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self) -> None:
        dados: dict[str, str] = {
            'nome': 'Felicity Jones',
            'assunto': 'Meu assunto',
        }
        request: HttpResponse = self.client.post(
            reverse_lazy('index'), data=dados
        )

        self.assertEquals(request.status_code, 200)
