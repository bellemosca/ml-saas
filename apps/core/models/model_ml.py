import pickle

from django.conf import settings
from django.db import models

from .. import constants


def owner_folder(instance, filename) -> str:
    return f'core/ml/{instance.owner_id}/{filename}'


class ModelML(models.Model):
    """Modelo de Machine learning"""

    # Campo id ou pk já é automaticamente criado
    nome = models.CharField(
        verbose_name='Nome do modelo',
        help_text='Nome a ser exibido para o usuário',
        max_length=100,
        blank=False,
    )
    description = models.CharField(
        verbose_name="descrição",
        max_length=500,
        null=False,
        blank=True,
        default='',
    )
    tipo = models.IntegerField(
        verbose_name='Tipo do modelo',
        help_text='Explicita se é um modelo de classificação ou regressão',
        choices=constants.ModelType,
    )
    is_public = models.BooleanField(
        verbose_name='é publico?',
        help_text='Define se pode ser acessado por um usuário anônimo',
        default=True,
        db_default=True,
    )
    arquivo = models.FileField(
        upload_to=owner_folder,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(auto_now=True, help_text='Ultima atualização')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Data de criação')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='models',
        help_text='Dono do modelo'
    )

    class Meta:
        verbose_name = 'Modelo de Machine Learn'
        verbose_name_plural = 'Modelos de Machine Learn'

    def __str__(self):
        return f'<{self.nome}>'


    _ml = None

    @property
    def model(self):
        if self._ml is None:
            with self.arquivo.file as f:
                self._ml = pickle.load(f)
        return self._ml

    def predict(self, *items):
        return self.model.predict(items)

    def predict_proba(self, *items):
        return self.model.predict_proba(items)
