# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class UserProfile(models.Model):
    highscore = models.IntegerField(default=0)
    user = models.OneToOneField(User)

    class Meta:
        verbose_name = _('UserProfile')
        verbose_name_plural = _('UserProfiles')

    def __unicode__(self):
        return u"%s - %s %s" % (self.user.username, self.user.first_name, self.user.last_name)


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return u"%s" % self.name


class Question(models.Model):
    text = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    committed_by = models.ForeignKey(UserProfile)
    accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __unicode__(self):
        return u"%s" % self.text[:50]


class Answer(models.Model):
    text = models.CharField(max_length=50)
    question = models.ForeignKey(Question)
    is_solution = models.BooleanField(default=False)
