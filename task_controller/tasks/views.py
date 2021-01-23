import logging
from datetime import datetime
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


class TaskIndex(ListView):
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


class GetSearchTask(APIView):
    """
        API TASK: Buscar tarea por contenido y fecha.
        fecha: se espera el formato YYYY/MM/DD
    """

    def get(self, request):
        content = request.query_params.get('content', None)
        date_create = request.query_params.get('date', None)
        if date_create is None:
            try:
                query = Task.objects.filter(
                    content__icontains=content,
                )
            except Task.DoesNotExist:
                logger.warning('400 en update task')
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                str_date = datetime.strptime(date_create, '%Y/%m/%d')
                query = Task.objects.filter(
                    content__icontains=content,
                    date_create__year=str_date.year,
                    date_create__month=str_date.month,
                    date_create__day=str_date.day,
                )
            except Task.DoesNotExist:
                logger.warning('400 en update task')
                return Response(status=status.HTTP_400_BAD_REQUEST)
        list_result_task = []
        for result_task in query:
            json_tasks = {
                'name': result_task.name,
                'content': result_task.content,
                'date_create': result_task.date_create,
                'status_task': result_task.status_task
            }
            list_result_task.append(json_tasks)
        return Response([list_result_task])
