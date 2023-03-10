from django.db import models

from tracker_app.models.projects import Project


class Issue(models.Model):
    summary = models.CharField(
        max_length=200,
        null=True,
        blank=False,
        verbose_name="Заголовок")
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name="Описание")
    status = models.ForeignKey(
        to='tracker_app.Status',
        related_name='issues',
        verbose_name='Статус',
        on_delete=models.PROTECT
    )
    type = models.ManyToManyField(
        to='tracker_app.Type',
        related_name='issues',
        verbose_name='Тип',
        blank=True
    )
    projects = models.ForeignKey(
        to='tracker_app.Project',
        related_name='issues',
        verbose_name='Проект',
        blank=True,
        on_delete=models.PROTECT
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Время создания")
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата и время обновления")
