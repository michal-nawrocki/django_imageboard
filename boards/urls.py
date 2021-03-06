from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "boards"
urlpatterns = [
    path("", views.index, name="index"),
    path("thread/<int:post_id>/", views.thread, name="thread")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
