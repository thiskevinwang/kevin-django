from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

# PART 3
# https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html#using-the-urls-api
def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        # from django.http import ...
        raise Http404
    return render(request, 'topics.html', {'board': board})