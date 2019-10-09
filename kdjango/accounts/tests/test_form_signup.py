from django.test import TestCase
from ..forms import SignUpForm

# This test is very strict. Why?
# 
# In the future, if we have to change the SignUpForm, to include
# the user's first and last name, we will probably end up having
# to fix a few test cases, even if we didn't break anything.

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

