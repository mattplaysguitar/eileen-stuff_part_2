from django.db import models

#3rd party
from ckeditor.fields import RichTextField


class TermsOfService(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(null=True, blank=True,)

