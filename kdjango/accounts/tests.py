from django.test import TestCase
from django.urls import resolve, reverse
from .views import signup
from django.contrib.auth.forms import UserCreationForm

class SignUpTests(TestCase):
    def setUp(self):
        # reverse()
        # https://docs.djangoproject.com/en/2.2/ref/urlresolvers/#reverse
        # 
        # reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)