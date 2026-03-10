from django.db import models


class ModelType(models.IntegerChoices):
    """Tipo do modelo"""
    CLASSIFICACAO = 0, 'Classificação'
    REGRESSAO = 1, 'Regressão'
