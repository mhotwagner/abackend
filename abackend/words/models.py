from django.db import models
from django.db.models import fields
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class Word(TimeStampedModel):
	word = fields.CharField(max_length=256, blank=False)

	def __str__(self):
		return self.word