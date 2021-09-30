from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from mixer.backend.django import mixer
from userapp.models import User

class TestUser(APITestCase):
    def test_get_detail(self):
        user = mixer.blend(User)
        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_user_guest(self):
        user = mixer.blend(User)
        response = self.client.put(f'/api/users/{user.id}/', {'email': 'admin@admin.ru'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_user_admin(self):
        user = mixer.blend(User)
        User.objects.create_superuser('admin', 'admin@admin.com', '12345')
        self.client.login(username='admin', password='12345')
        response = self.client.put(f'/api/users/{user.id}/', {'username': 'name',
                                                                'first_name': 'f_n',
                                                                'last_name': 'l_n'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        self.assertEqual(response.data.get('username'), 'name')
        self.assertEqual(response.data.get('first_name'), 'f_n')
        self.assertEqual(response.data.get('last_name'), 'l_n')