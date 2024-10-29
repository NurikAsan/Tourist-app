from django.db import models


class Base(models.Model):
    verbose_name = None
    title = models.CharField(max_length=40, verbose_name=verbose_name)

    def __str__(self) -> str:
        return self.title

    class Meta:
        abstract = True
