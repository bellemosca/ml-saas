import os
import sys
import django
import pickle
import numpy as np

# Configura o ambiente do Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.core.files.base import ContentFile
from apps.core.models import ModelML
from apps.manager.models import CustomUser
from apps.core.constants import ModelType
from sklearn.ensemble import RandomForestClassifier


def seed_db():
    print("Iniciando o preenchimento (seed) do banco de dados...")

    # Criação do superusuário padrão (admin / admin)
    user, created = CustomUser.objects.get_or_create(username="admin")
    if created:
        user.set_password("admin")
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print("Superusuário 'admin' criado com senha 'admin'.")
    else:
        print("Superusuário 'admin' já existia.")

    # Criação de um modelo ML treinando um RandomForest simples para não dar erro na tela
    print("Gerando um modelo preditivo sintético (Random Forest)...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    # Gerando dados sintéticos (8 features) pra treinar o modelo de classificacao (diabetes ou nao)
    X_dummy = np.random.rand(100, 8) * 100
    y_dummy = np.random.randint(0, 2, 100)
    clf.fit(X_dummy, y_dummy)

    model_bytes = pickle.dumps(clf)

    # Inserção no banco
    if not ModelML.objects.filter(nome="Modelo Preditivo Base (RF)").exists():
        model_ml = ModelML(
            nome="Modelo Preditivo Base (RF)",
            description="Modelo de Random Forest gerado via seed para classificação.",
            tipo=ModelType.CLASSIFICACAO,
            is_public=True,
            owner=user,
        )
        model_ml.arquivo.save("rf_model_seed.pkl", ContentFile(model_bytes))
        model_ml.save()
        print("Modelo ML de Classificação criado com sucesso!")
    else:
        print("O Modelo ML já existia.")

    print("Seed concluído com sucesso!")


if __name__ == "__main__":
    seed_db()
