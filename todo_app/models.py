from django.db import models
from django.utils import timezone

# Create your models here.
class TodoTask(models.Model):
    created_at = models.DateTimeField("Created at")
    is_done = models.BooleanField("Is Done Task", default=False)
    title = models.CharField("Title", max_length=500)
    is_priority = models.BooleanField("Is Priority", default=False)
    details = models.TextField("Details")

    def __str__(self) -> str:
        """Returns a string representation"""
        date = timezone.localtime(self.created_at)
        return f"'{self.title}' created at {date.strftime('%A, %d %B, %Y at %X')} with details '{self.details}'"


