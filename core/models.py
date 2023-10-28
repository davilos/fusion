import uuid
from typing import Tuple

from stdimage.models import StdImageField

from django.db import models


def get_file_path(_instance, filename: str) -> str:
    ext: str = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract: bool = True


class Servico(Base):
    ICONE_CHOICES: Tuple[Tuple[str, str], ...] = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name: str = 'Serviço'
        verbose_name_plural: str = 'Serviços'

    def __str__(self) -> str:
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name: str = 'Cargo'
        verbose_name_plural: str = 'Cargos'

    def __str__(self) -> str:
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey(
        'core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE
    )
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField(
        'Imagem',
        upload_to=get_file_path,
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}},
    )
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name: str = 'Funcionário'
        verbose_name_plural: str = 'Funcionários'

    def __str__(self) -> str:
        return self.nome


class Feature(Base):
    ICONE_CHOICES: Tuple[Tuple[str, str], ...] = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Aparelhos'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Design'),
    )

    feature = models.CharField('Feature', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name: str = 'Feature'
        verbose_name_plural: str = 'Features'

    def __str__(self) -> str:
        return self.feature
