from django.db import models

from common.models.abstracts.create_update_abstract_model import CreateUpdateAbstractModel
from common.models.abstracts.index_abstract_model import IndexAbstractModel


class Word(IndexAbstractModel, CreateUpdateAbstractModel):
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=255, null=True, blank=True)
    example = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.word