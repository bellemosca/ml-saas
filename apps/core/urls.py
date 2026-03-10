from django.contrib.auth.decorators import login_not_required
from django.urls import path
from django.views.generic import TemplateView
import numpy as np
from . import views
from .questions import DIABETES

app_name = 'core'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name="question_list_view"),
    path('<int:id>/', views.QuestionDetailView.as_view(), name="question_detail_view"),
    path(
        'teste/',
        login_not_required(TemplateView.as_view(
            template_name='core/question/answer.html',
            extra_context={
                'question': DIABETES,
                'resultado': list(map(
                    lambda r: ({'nome': f'classificador-{r}'}, int(r>50), [100-r, r]),
                    np.random.random_integers(0, 101, 20)
                )),
            },
        ))
    ),
]
