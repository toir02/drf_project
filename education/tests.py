from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Lesson


class LessonTestCase(APITestCase):

    def setUp(self):
        pass

    def test_create_lesson(self):
        """test for create lesson"""
        data = {
            "title": "test",
            "description": "test",
            "link": "https://www.youtube.com/watch?v=_x8DV1WLtks&t=142s",
        }

        url = reverse("education:lesson_create")
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(), {"id": 1,
                                           "title": "test",
                                           "description": "test",
                                           "image": None,
                                           "link": "https://www.youtube.com/watch?v=_x8DV1WLtks&t=142s",
                                           "user": None,
                                           "course": None})

    def test_get_lessons(self):
        """test for get lessons"""
        url = reverse("education:lessons")
