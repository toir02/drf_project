from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Lesson, Subscription, Course
from users.models import User


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
        """test for delete lessons"""

        Lesson.objects.create(id=1, title='no test', description='test', image=None,
                              link='https://www.youtube.com/watch?v=_x8DV1WLtks&t=142s', user=None, course=None)

        url = reverse("education:lesson_delete", kwargs={"pk": 1})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.data = {
            "user": 1,
            "course": 1,
            "is_active": True
        }

        User.objects.create(email='test@test.com', password='test')
        Course.objects.create(title="test", description="test")

    def test_create_subscription(self):
        """test for create subscription"""

        url = reverse("education:create-subscription")

        response = self.client.post(url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(), {'id': 1, 'is_active': True, 'user': 1, 'course': 1})

    def test_delete_subscription(self):
        """test for delete subscription"""
        user = User.objects.get(pk=1)
        course = Course.objects.get(pk=1)

        Subscription.objects.create(user=user, course=course, is_active=True)

        url = reverse("education:delete-subscription", kwargs={"pk": 1})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
