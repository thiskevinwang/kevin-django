from django.urls import reverse, resolve
from django.test import TestCase

from .views import home, board_topics
from .models import Board

# add 1 test
# https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html#testing-the-homepage
# 
'''
cd kdjango
python manage.py test
# or
python manage.py test --verbosity=2 
'''
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

# Add tests
# https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html#using-the-urls-api
# 
# this requires the import:
# `from .models import Board`
class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # this will fail if you don't have 99 boards
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_board_topics_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        # this requires
        # from .views, import ..., board_topics
        self.assertEquals(view.func, board_topics)