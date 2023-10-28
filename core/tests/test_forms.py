from core.forms import ContatoForm
from django.test import TestCase

CONTATO = ContatoForm


class ContatoFormTestCase(TestCase):
    def setUp(self) -> None:
        self.nome: str = 'Felicity Jones'
        self.email: str = 'felicity@gmail.com'
        self.assunto: str = 'Um assunto qualquer'
        self.mensagem: str = 'Uma mensagem qualquer'

        self.dados: dict[str, str] = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }

        self.form: CONTATO = ContatoForm(
            data=self.dados
        )  # ContatoForm(request.POST)

    def test_send_mail(self) -> None:
        form1: CONTATO = ContatoForm(data=self.dados)
        form1.is_valid()

        form2: CONTATO = self.form
        form2.is_valid()

        self.assertEquals(form1.is_valid(), form2.is_valid())
