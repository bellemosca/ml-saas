"""
URL configuration for ml_saas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_not_required
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("manager/", include("apps.manager.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path(
        "",
        login_not_required(
            RedirectView.as_view(
                pattern_name="core:question_list_view", permanent=False
            )
        ),
        name="home_view",
    ),
    path("predict/", include("apps.core.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.http import FileResponse

    @login_not_required
    def favicon_view(request):
        return FileResponse(
            open(f"{settings.STATIC_ROOT}/favicon.ico", "rb"),
            as_attachment=True,
            filename="favicon.ico",
            content_type="image/vnd.microsoft.icon",
        )

    urlpatterns += [
        path("favicon.ico", favicon_view),
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
