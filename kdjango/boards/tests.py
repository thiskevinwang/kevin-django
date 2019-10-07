from django.urls import reverse, resolve
from django.test import TestCase

from .views import home

# add 1 test
# https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html#testing-the-homepage
# 
'''
cd kdjango
python manage.py test
'''
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)