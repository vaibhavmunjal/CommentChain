from django.db import models


class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    path = models.CharField(blank=True, editable=False, max_length=300)

    def __str__(self):
        return str(f"content={self.content}\npath={self.path}")

    class Meta:
        ordering = ["path"]
