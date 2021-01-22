from django.db import models


class Task(models.Model):
    STATUS_TASK_CHOICE = ((True, "Completada"), (False, "Pendiente"))

    name = models.CharField(
        max_length=144,
        verbose_name="Nombre"
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )
    content = models.CharField(
        max_length=144,
        verbose_name="Contenido"
    )
    status_task = models.BooleanField(
        choices=STATUS_TASK_CHOICE,
        verbose_name="Estado",
        default=False
    )

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = [
            "-date_create",
        ]

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name