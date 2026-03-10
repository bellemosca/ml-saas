from dataclasses import dataclass

from django.forms import Form
from ..constants import ModelType


@dataclass
class Question:
    form_class: type[Form]
    tipo_modelo: ModelType
    id: int
    title: str
    context: str
    objective: str
    about: str
