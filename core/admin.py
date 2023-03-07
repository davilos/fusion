from django.contrib import admin

from .models import Cargo, Feature, Funcionario, Servico


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ('feature', 'icone', 'ativo', 'modificado')
