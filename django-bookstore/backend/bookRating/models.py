from django.db import models
from books.models import Book
from users.models import Customer

class Comment(models.Model):
    author = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    score = models.PositiveSmallIntegerField(
        choices=(
            (1, "*"),
            (2, "**"),
            (3, "***"),
            (4, "****"),
            (5, "*****"),
        )
    )
    title = models.CharField(max_length=180)
    content = models.CharField(max_length=900)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return ", ".join((str(self.author), str(self.book)))

    class Meta:
        ordering = ["-timestamp"]
        unique_together = ("author", "book",)
