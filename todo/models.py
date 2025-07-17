from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=timezone.now)
    due_at = models.DateTimeField(null=True, blank=True)
    num_like = models.IntegerField(default=0)
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Middle'),
        (3, 'High'),
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)

    def is_overdue(self, dt):
        if self.due_at is None:
            return False
        return self.due_at < dt
