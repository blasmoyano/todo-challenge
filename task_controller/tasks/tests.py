from django.test import TestCase
from .models import Task
from datetime import datetime
from rest_framework.test import APIClient
from rest_framework import status
from urllib.parse import urljoin


class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(
            name="test_model",
            content="test_model",
            date_create=datetime.now(),
            status_task=True
        )

    def test_task_create(self):
        test = Task.objects.get(name="test_model")
        self.assertTrue(isinstance(test, Task))
        self.assertEqual(test.__unicode__(), "test_model")


class TaskApiTestCase(TestCase):
    def setUp(self):
        self.url = 'http://localhost:8080/PROD_control_tareas/tasks/api/'
        Task.objects.create(
            name="test_model",
            content="test_model",
            date_create=datetime.now(),
            status_task=True
        )

    def test_api_list_task(self):
        url_api = urljoin(self.url, 'tareas/')
        client = APIClient()
        response = client.get(url_api)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_api_create_task(self):
        url_api = urljoin(self.url, 'crear_tareas/')
        client = APIClient()
        response = client.post(
            url_api,
            data={
                'name': "create_task",
                "content": "create_content"
            }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_api_fail_create_task(self):
        url_api = urljoin(self.url, 'crear_tareas/')
        client = APIClient()
        response = client.post(
            url_api,
            data={
                'name': "create_task",
            }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
