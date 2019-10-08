from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})