from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Lesson


class LessonTestCase(APITestCase):

    def setUp(self):
        self.data = {
            "title": "test",
            "description": "test",
            "link": "https://www.youtube.com/watch?v=_x8DV1WLtks&t=142s",
        }

    def test_create_lesson(self):
        """test for create lesson"""

        url = reverse("education:lesson_create")
        response = self.client.post(url, data=self.data)

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
        Lesson.objects.create(id=1, title='test', description='test', image=None,
                              link='https://www.youtube.com/watch?v=_x8DV1WLtks&t=142s', user=None, course=None)

        url = reverse("education:lesson_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': 1, 'title': 'test', 'description': 'test', 'image': None,
             'link': 'https://www.youtube.com/watch?v=_x8DV1WLtks&t=142s', 'user': None, 'course': None}]}
                         )

    def test_update_lessons(self):
        """test for update lessons"""
        Lesson.objects.create(id=1, title='no test', description='test', image=None,
                              link='https://www.youtube.com/watch?v=_x8DV1WLtks&t=142s', user=None, course=None)

        url = reverse("education:lesson_edit", kwargs={"pk": 1})
        response = self.client.put(url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), {'id': 1, 'title': 'test', 'description': 'test', 'image': None,
                                           'link': 'https://www.youtube.com/watch?v=_x8DV1WLtks&t=142s', 'user': None,
                                           'course': None}
                         )

    def test_delete_lessons(self):
        pass