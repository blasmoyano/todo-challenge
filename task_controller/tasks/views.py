import logging
from .models import Task
from .tasksFilter import TaskFilter
from .serializer import TaskSerializer
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)


class TaskIndex(ListView): # LoginRequiredMixin
    model = Task
    template_name = "tasks/index.html"
    paginate_by = 10
    lookup_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        logger.warning('TaskIndex')
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        print(self.request.GET)
        context['tags_filter'] = \
            TaskFilter(self.request.GET)
        return context


class TaskCreate(CreateView):
    template_name = 'tasks/form_tasks.html'
    model = Task
    success_url = reverse_lazy('task_index')
    fields = [
        'name',
        'content',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_form'] = "Crear"
        logger.warning('Se creo contenido')
        return context


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskEdit(UpdateView):
    template_name = 'tasks/form_tasks.html'
    model = Task
    success_url = reverse_lazy('task_index')
    fields = ["name", "content", "status_task"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_form'] = "Editar"
        return context


# API

class GetAllTask(generics.ListAPIView):
    """
    API TASK: Devuelve todas las tareas.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.filter()


class PostCreateTask(generics.ListCreateAPIView):
    """
    API TASK: Crear tarea
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['post', 'put']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DelTask(generics.RetrieveDestroyAPIView):
    """
    API TASK: Borrar tarea
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class PostUpdateTask(APIView):
    """
        API TASK: Completa tarea
    """

    def put(self, request, id):
        id_task = id
        try:
            update_task = Task.objects.get(id=id_task)
            update_task.status_task = True
            update_task.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            logger.warning('400 en update task')
            return Response(status=status.HTTP_400_BAD_REQUEST)
