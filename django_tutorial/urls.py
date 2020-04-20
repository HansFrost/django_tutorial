from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("calc.urls")),
    path("calc/", include("calc.urls")),
    path("polls/", include("polls.urls")),
    path("travello/", include("travello.urls")),
    path("morgenmad/", include("madplan.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

