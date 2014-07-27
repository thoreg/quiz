from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from quizshowdown.quiz.api import router

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^addi/', include(admin.site.urls)),
    url(r'^$', 'quizshowdown.quiz.views.index', name="index"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
