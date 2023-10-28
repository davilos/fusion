import uuid
from typing import Any

from model_mommy import mommy

from core.models import get_file_path
from django.test import TestCase


class GetFilePathTestCase(TestCase):
    def setUp(self) -> None:
        self.filename: str = f'{uuid.uuid4()}.png'

    def test_get_file_path(self) -> None:
        arquivo: str = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):
    def setUp(self) -> None:
        self.servico: Any = mommy.make('Servico')

    def test_str(self) -> None:
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):
    def setUp(self) -> None:
        self.cargo: Any = mommy.make('Cargo')

    def test_str(self) -> None:
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):
    def setUp(self) -> None:
        self.funcionario: Any = mommy.make('Funcionario')

    def test_str(self) -> None:
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class FeatureTestCase(TestCase):
    def setUp(self) -> None:
        self.feature: Any = mommy.make('Feature')

    def test_str(self) -> None:
        self.assertEquals(str(self.feature), self.feature.feature)
