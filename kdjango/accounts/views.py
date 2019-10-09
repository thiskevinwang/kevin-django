from django.contrib.auth import login
from django.shortcuts import render, redirect

# import the custom form that extends UserCreationForm
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # If the form is valid...
        if form.is_valid():
            # a *User* instance is created 
            user = form.save()
            # The created user is passed as an argument to the
            # auth `login` function, manually authenticating the user.
            login(request, user)
            # After that, the view redirects the user to the homepage,
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})