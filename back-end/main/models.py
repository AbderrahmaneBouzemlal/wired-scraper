from django.db import models
from django.urls import reverse
import uuid

class Wired(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True)
    index = models.IntegerField()
    title = models.CharField(max_length=255, unique=True)
    URL = models.URLField()
    date_of_publish = models.DateField(auto_now=False, auto_now_add=False)
    picture = models.ImageField(upload_to='images/', default="images/default.jpeg")

    class Meta:
        verbose_name = "Wired"
        verbose_name_plural = "Wired"
        ordering = ['-date_of_publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Wired_detail", kwargs={"pk": self.pk})
