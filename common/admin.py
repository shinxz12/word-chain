from django.contrib import admin

from common.models.word_model import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass