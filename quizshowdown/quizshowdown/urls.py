from django.conf.urls import patterns, include, url

from django.contrib import admin

from quizshowdown.quiz.api import router

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^addi/', include(admin.site.urls)),
)
