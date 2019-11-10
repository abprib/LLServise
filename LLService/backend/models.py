from django.db import models
from registrations.models import User
from words.models import Word

class Main(models.Model):
    word = models.ForeignKey(
        Word,
        related_name='words',
        on_delete=models.CASCADE,
    )
    send_time = models.DateTimeField()
    if_send = models.BooleanField(
        default=False,
    )

