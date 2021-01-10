from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    A contact model for storing enquiry/contact info
    """

    class Meta:
        verbose_name = 'Inbox'
        verbose_name_plural = 'Messages'

    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name