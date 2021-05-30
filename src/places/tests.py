import tempfile
from django.test import TestCase
from django.contrib.gis.geos import Point
from .forms import CreatePlaceForm
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Place, User


class PlacesListViewTest(TestCase):

    def setUp(self):

        image = tempfile.NamedTemporaryFile(suffix=".jpg").name

        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        Place.objects.create(title='test1', description='test1', coordinate=Point(50, 70), user=test_user2, image=image)
        Place.objects.create(title='test2', description='test2', coordinate=Point(50, 70), user=test_user2, image=image)

    def test_redirect_if_not_logget_in(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/about?next=/')

    def test_logged_user_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/')

        self.assertEqual(str(response.context['user']), 'testuser1')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'places/places_list.html')

    def test_users_showing_places(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/')

        self.assertEqual(str(response.context['user']), 'testuser1')

        self.assertEqual(response.status_code, 200)

        self.assertTrue('object_list' in response.context)
        self.assertEqual(len(response.context['object_list']), 0)

        self.client.login(username='testuser2', password='2HJ1vRV0Z&3iD')

        response = self.client.get('/')

        self.assertTrue('object_list' in response.context)
        self.assertEqual(len(response.context['object_list']), 2)


class CreatePlaceViewTest(TestCase):

    def test_succesfuly_create_place(self):

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')

        form = CreatePlaceForm(data={'title': 'test1',
                                     'description': 'test1',
                                     'coordinate': Point(50, 50)},
                               files={'image': uploaded})

        self.assertTrue(form.is_valid())

    def test_create_place_with_error(self):
        form = CreatePlaceForm(data={'title': 'test1',
                                     'description': 'test1',
                                     'coordinate': Point(50, 50)})

        self.assertFalse(form.is_valid())
