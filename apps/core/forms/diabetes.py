from django import forms

fields: dict[str, int | float] = {
    'Pregnancies': 6,
    'Glucose': 148,
    'BloodPressure': 72,

    'SkinThickness': 35,
    'Insulin': 0,
    'BMI': 33.6,
    'DiabetesPedigreeFunction': 0.627,

    'Age': 50,
}


class DiabetesForm(forms.Form):
    num_pregnancies = forms.IntegerField(
        label='n° de gravidezes',
        min_value=0, max_value=20, required=True,
        help_text='Quantidade de gravidez que teve',
    )
    num_glucose = forms.IntegerField(
        label='Glicose',
        label_suffix='mg',
        min_value=0, max_value=200, required=True,
        help_text='Concentração de glicose plasmática após 2 horas em um teste oral de tolerância à glicose',
    )
    blood_pressure = forms.IntegerField(
        label='Pressão sanguinea',
        label_suffix='(mm Hg)',
        min_value=0, max_value=150, required=True,
        help_text='Pressão arterial diastólica',
    )
    skin_thickness = forms.IntegerField(
        label='Espessura de pele',
        label_suffix='(mm)',
        min_value=0, max_value=100, required=True,
        help_text='Espessura da prega cutânea do tríceps.',
    )
    insulin = forms.FloatField(
        label='Insulina',
        label_suffix='(µU/ml)',
        min_value=0, max_value=1000,
        help_text='Insulina sérica de 2 horas.'
    )
    imc = forms.FloatField(
        label='IMC',
        min_value=0, max_value=100,
        label_suffix='(peso em kg/(altura em m)^2)',
        help_text='Indice de Massa Corporal'
    )
    pedigree_diabetes = forms.FloatField(
        label='pedigree',
        min_value=0, max_value=3,
        help_text='Função de pedigree de diabetes',
    )
    idade = forms.IntegerField(
        label='idade',
        label_suffix='(anos)',
        max_value=100, min_value=0, required=True,
    )
