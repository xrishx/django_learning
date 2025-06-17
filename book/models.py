from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    TYPE_CHOICES = {
        ('hardcover', "Hardcover")
        ('paperback', 'Paperback')
    }

    name = models.CharField(max_length=255, help_text='Name of the book')
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    