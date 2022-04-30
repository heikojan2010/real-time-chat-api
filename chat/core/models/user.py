import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from .message import Message
import uuid
from django.conf import settings

# from chat.core.models.conversation import Conversation


@python_2_unicode_compatible
class User(AbstractUser):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='logged_in_user', 
        on_delete=models.PROTECT, 
        null=True,
        blank=True
        )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    last_read_date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False
    )
    online = models.BooleanField(null=False, blank=False, default=False)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def read(self):
        self.last_read_date = timezone.now()
        self.save()

    def unread_messages(self):
        return Message.objects.filter(created_at__gt=self.last_read_date) \
                              .count()
