from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path(
        'index',
        views.TaskIndex.as_view(),
        name="task_index"
    ),
    path(
        'create',
        views.TaskCreate.as_view(),
        name="task_create"
    ),
    path(
        'delete/<int:pk>',
        views.TaskDelete.as_view(),
        name="task_delete"
    ),
    path(
        'edit/<int:pk>',
        views.TaskEdit.as_view(),
        name="task_edit"
    ),
    path(
        'api/tareas/',
        views.GetAllTask.as_view()
    ),
    path(
        'api/crear_tareas/',
        views.PostCreateTask.as_view()
    ),
    path(
        'api/borrar_tarea/<int:id>',
        views.DelTask.as_view()
    ),
    path(
        'api/update_tarea/<int:id>',
        views.PostUpdateTask.as_view()
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
