from typing import Any

from django.contrib.auth.decorators import login_not_required
from django.forms import Form
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from ..models import ModelML
from ..questions import QUESTIONS_MAP


@method_decorator(login_not_required, name="dispatch")
class QuestionDetailView(FormView):
    template_name = 'core/question/form.html'

    def get_question(self):
        return QUESTIONS_MAP.get(self.kwargs.get('id'))

    def get_form_class(self) -> type[Form]:
        return getattr(self.get_question(), 'form_class', Form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        if (q := self.get_question()) is not None:
            context['question'] = q
        else:
            # Se question for None, então Form é inválido
            context.pop('form')

        return context

    def _get_queryset(self):
        return ModelML.objects.filter(is_public=True)

    def _format_data(self, cleaned_data: dict):
        return [value for value in cleaned_data.values()]

    def form_valid(self, form: Form):
        # formatar dados para input do modelo
        data = self._format_data(form.cleaned_data)

        # Carregar modelos
        assert (questao := self.get_question()) is not None, f'Não há questão com este id: "{self.kwargs.get("id")}"'

        modelos = self._get_queryset().filter(tipo=questao.tipo_modelo).all()

        # fazer classificação
        context = self.get_context_data()
        context['question'] = questao
        context["resultado"] = [
            (m, *m.predict(data), *(m.predict_proba(data) * 100))
            for m in modelos
        ]
        return render(
            request=self.request,
            template_name='core/question/answer.html',
            context=context,
        )
