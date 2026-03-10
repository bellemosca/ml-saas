from typing import Any

from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from ..questions import QUESTIONS_MAP


@method_decorator(login_not_required, name="dispatch")
class QuestionListView(TemplateView):
    template_name = 'core/question/list.html'

    _data = list(QUESTIONS_MAP.values())

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['questions'] = self._data
        return context
