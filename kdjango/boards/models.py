from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    # unique=True 
    # - forces uniqueness at the database level
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    # The __str__ method is a String representation of an object. 
    # We can use the board name to represent it.
    def __str__(self):
        return self.name

    # $ python manage.py shell
    # >>> from boards.models import Board
    # >>> Boards.objects.all()
    '''
    <QuerySet [<Board: Django>, <Board: Python>]>
    '''

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)

    # ForeignKey
    # - Used to create a relationship between models.
    # 
    # - It will create a link between models and create a 
    # - proper relationship at the database level.
    #  
    # - This expects a positional parameter with the reference to 
    # - the model it will relate to.
    # 
    # Example:
    # - the board field is a ForeignKey to the Board model. It is
    # - telling Django that a topic insntance relates to only
    # - ony **Board** instance. The `related_name` parameter
    # - will be used to create a reverse relationship where the
    # - Board instances will have access to a list of Topic
    # - instances that belong to it.
    # 
    # related_name (optional param)
    # - If you don't set it, Django will generate it with the name:
    # `(class_name)_set`
    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='topics') # Board > topics (or topic_set, if not specified) 
    starter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='topics')

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, related_name='posts')
    # auto_now_add (optional param)
    # - This will instruct Django to set the current date and time 
    # - when a `Post` object is created.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='+')