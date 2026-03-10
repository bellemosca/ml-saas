# Trabalho Final do Curso de Extensão - Introdução a Ciência de dados

### Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE)

## ⚙️ Como rodar o projeto (Setup)

Este projeto utiliza o [uv](https://docs.astral.sh/uv/) para gerenciamento rápido de dependências e ambiente virtual.

### Inicialização Rápida

Instale as dependências usando o `uv`:

```bash
# Baixa as dependências e cria um ambiente virtual automaticamente (.venv)
uv sync

# Para popular o banco com o usuário "admin" (senha: "admin") e treinar um modelo base
uv run python seed/seed_db.py

# Para iniciar o servidor de desenvolvimento (já checa e roda migrações também)
uv run python dev.py
```

#### Notebook e modelos

> ⚠️ Para modelos e notebooks exploratórios.

Se desejar trabalhar separadamente com os notebooks (`.ipynb`), você pode instalar as bibliotecas de dados assim:

```bash
uv add --dev notebook seaborn pandas
```

_Nota: a biblioteca `scikit-learn` já é nativa do projeto e estará disponível nos notebooks! Para acessar o notebook depois, basta rodar `uv run jupyter notebook`._

---

### 👥 Equipe:

- Anilton Magalhães de Castro
- Jeferson Nóbrega da Rocha
- Maria Isabelle Mosca de Araújo
- Roseline Torres

## 🎯 Objetivos

O objetivo do nosso projeto é criar um SaaS onde iremos implementar através de uma API um modelo de aprendizado de máquina capas de prever a ocorrência de diabetes em pacientes, com base em variáveis clínicas. Iremos, antes de tudo, fazer a comparação entre diferentes algoritmos, buscar identificar o melhor modelo com melhor desempenho preditivo, priorizando métricas adequadas a problemas da área médica, como o recall da classe positiva.

## 📊 Dataset

O dataset utilizado é o **Pima Indians Diabetes Dataset**, amplamente utilizado em estudos de Machine Learning para classificação.

Ele contém informações médicas de pacientes do sexo feminino com pelo menos 21 anos de idade.

Variáveis presentes no dataset:

| Variável                 | Descrição                                    |
| ------------------------ | -------------------------------------------- |
| Pregnancies              | Número de gestações                          |
| Glucose                  | Concentração de glicose no sangue            |
| BloodPressure            | Pressão arterial                             |
| SkinThickness            | Espessura da dobra cutânea                   |
| Insulin                  | Nível de insulina                            |
| BMI                      | Índice de massa corporal                     |
| DiabetesPedigreeFunction | Histórico familiar de diabetes               |
| Age                      | Idade                                        |
| Outcome                  | Resultado (0 = não diabético, 1 = diabético) |

Fonte: [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data)

---

# 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# 🚀 Pipeline do Projeto

1. Importação das bibliotecas
2. Carregamento do dataset
3. Análise exploratória dos dados (EDA)
4. Tratamento de dados
5. Preparação das variáveis
6. Treinamento dos modelos
7. Avaliação de desempenho
8. Comparação de modelos
9. Salvamento do modelo

---

# 🔎 Análise Exploratória (EDA)

Durante a análise exploratória foram investigados:

- Distribuição das variáveis ( com boxplot)
- Relação entre variáveis (correlação com heatmap)
- Presença de valores inconsistentes
- Balanceamento da variável alvo (gráfico de barras de Outcome)

Também foi identificado que algumas variáveis possuíam **valores zero biologicamente impossíveis**, como:

- Glucose
- BloodPressure
- SkinThickness
- BMI
- Insulin

Esses valores foram tratados durante a etapa de pré-processamento.

---

# 🧹 Tratamento de Dados

Valores iguais a zero em variáveis como glicose e pressão arterial não são fisiologicamente plausíveis, sendo tratados como valores ausentes e substituídos por medidas estatísticas adequadas. Além do mais, modelos de machine learning não rodam com valores NaN, sendo assim, iremos substituir pela mediana.

Mas por que a mediana? Ela é muito mais "robusta" e não se deixa levar por valores muito altos ou muito baixos, ou seja, outliers. Por isso, em saúde, usamos muito a mediana para preencher dados faltantes.

---

# 🤖 Modelos Utilizados

Foram testados diferentes modelos de classificação:

- Regressão Logística
- Random Forest
- Gaussian Naive Bayes
- XGBoost

Os testes foram realizados de duas formas:

1. **Sem intervenção nos classificadores**:
   Os modelos apresentaram uma alta acurácia simplesmente classificando a maioria dos casos como "Saudáveis", resultando em um Recall perigosamente baixo para a classe de interesse (diabéticos).

2. **Com intervenção nos classificadores**:
   Para mitigar esse problema e lidar com o leve desbalanceamento do dataset, realizamos intervenções diretas nos hiperparâmetros de sensibilidade:

- ⚖️ **Pesos de Classe** (`class_weight='balanced'`): Aplicado na Regressão Logística e Random Forest para forçar o algoritmo a penalizar mais severamente os erros na classe minoritária.
- ⚖️ **Escalonamento de Peso** (`scale_pos_weight`): No XGBoost, ajustamos a balança interna do modelo com base na proporção real entre saudáveis e doentes.
- 🛠️ **Regularização e Profundidade**: Reduzimos a profundidade das árvores (`max_depth`) no XGBoost para evitar o overfitting.

---

# 📈 Avaliação dos Modelos

Os modelos foram avaliados utilizando métricas de classificação e apresentando os seguintes resultados:

| Modelo               | Acurácia | Recall | Precision | F1-Score |
| :------------------- | :------- | :----- | :-------- | :------- |
| Logistic Regression  | 0.701    | 0.709  | 0.565     | 0.629    |
| Random Forest        | 0.760    | 0.673  | 0.661     | 0.667    |
| Gaussian Naive Bayes | 0.753    | 0.673  | 0.649     | 0.661    |
| XGBoost              | 0.701    | 0.764  | 0.560     | 0.646    |

### 🔄 Validação cruzada (Acurácia Média - 5 Folds):

- **Logistic Regression**: 75.41% (+/- 4.41%)
- **Random Forest**: 76.39% (+/- 5.78%)
- **Gaussian Naive Bayes**: 74.76% (+/- 4.37%)
- **XGBoost**: 75.90% (+/- 8.31%)

Essas métricas ajudaram a avaliar qual modelo foi melhor na identificação correta de pacientes com diabetes.

---

# 🏆 Resultados

A escolha do **Random Forest** como modelo de produção justifica-se pelo seu desempenho superior em acurácia média (76.39%), seu equilíbrio entre sensibilidade e precisão, e sua robustez contra outliers devido às divisões hierárquicas. Enquanto o XGBoost demonstrou maior volatilidade, o Random Forest provou ser uma solução mais estável para integração em um ambiente de software médico (SaaS). 🏥✨

---
