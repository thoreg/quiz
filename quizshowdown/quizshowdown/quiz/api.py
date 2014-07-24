# -*- coding: utf-8 -*-
from rest_framework import viewsets, routers

from .models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    model = Question


router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
