from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home(request):
	boards = Board.objects.all()
	# return render(request, 'home.html', {'templateVar': boards})

	boards_names = list()
	
	for board in boards:
		boards_names.append(board.name)

	response_html = '<br>'.join(boards_names)

	return HttpResponse(response_html)

# PART 3
# https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html#using-the-urls-api
def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})