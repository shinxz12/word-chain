from django.db import models


class IndexAbstractModel(models.Model):
    index = models.PositiveIntegerField(default=1)

    class Meta:
        abstract = True
