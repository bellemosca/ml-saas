from ..constants import ModelType
from ..forms import DiabetesForm
from .question_base import Question

DIABETES = Question(
    form_class=DiabetesForm,
    tipo_modelo=ModelType.CLASSIFICACAO,
    id=1,
    title='Classificação de diabetes baseado no Pima Indians Diabetes Database',
    context=(
        'O diabetes é uma doença crônica de grande impacto na saúde pública, cujo diagnóstico precoce é essencial para prevenir complicações. '
        'Nesse contexto, técnicas de Ciência de Dados e Aprendizado de Máquina podem auxiliar na análise de dados clínicos e no apoio à tomada de decisão. '
    ),
    objective=(
        'O objetivo deste trabalho é desenvolver e avaliar modelos de aprendizado de máquina para prever a ocorrência de diabetes em pacientes, utilizando variáveis clínicas. '
        'A análise compara diferentes algoritmos, priorizando métricas relevantes para a área médica, como o recall da classe positiva. '
        'Trata-se de um problema de Classificação, no qual o modelo deve identificar se um paciente pertence à classe diabético ou não diabético. '
    ),
    about=(
        'O objetivo do conjunto de dados é prever, por meio de diagnóstico, se um paciente tem ou não diabetes, com base em certas medidas diagnósticas incluídas no conjunto de dados. '
        'Diversas restrições foram impostas à seleção desses casos a partir de um banco de dados maior. '
        'Em particular, todos os pacientes aqui são mulheres com pelo menos 21 anos de idade e de ascendência indígena Pima.'
    ),
)
