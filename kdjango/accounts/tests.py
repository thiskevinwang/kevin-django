from django.test import TestCase
from django.urls import resolve, reverse
from .views import signup
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.models import User

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
        self.assertIsInstance(form, SignUpForm)

# Part 4 - Sign Up - Testing the Sign Up View
# https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html#testing-the-sign-up-view

# Test a successful sign up
class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@johnmail.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456',
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')
    
    def test_redirection(self):
        '''
        A valid for msubmission should redirect the user to the home page
        '''
        self.assertRedirects(self.response, self.home_url)
    
    def test_user_creation(self):
        self.assertTrue(User.objects.exists())
    
    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  # submit an empty dictionary
        
    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())
        