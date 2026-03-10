from django.conf import settings


def project_title(request):
    return {
        'PROJECT_TITLE': 'MedPredict',
        'PROJECT_NAME': 'MedPredict',
        'DEFAULT_PROJECT_TITLE': 'MedPredict'
    }


def auth_urls(request):
    return {
        'LOGIN_URL': settings.LOGIN_URL,
        'LOGOUT_URL': settings.LOGOUT_URL,
    }
