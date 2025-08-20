from django.db import models
from django.utils import timezone

class ReportHistory(models.Model):
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(default=timezone.now)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.file_name} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
