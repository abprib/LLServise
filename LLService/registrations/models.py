from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    reg_key = models.CharField(
        _('Registration key'),
        max_length=10,
    )
    chat_id = models.IntegerField(
        _('Telegram User ID'),
        blank=True,
        null=True,
    )

