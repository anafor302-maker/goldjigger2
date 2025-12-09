import uuid
from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Cocktail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    ingredients = models.JSONField()   # [{"name":"vodka","amount":"50ml"}, ...]
    instructions = models.TextField(null=True, blank=True)
    tags = models.JSONField(default=list, blank=True)
    source = models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)
    source_url = models.URLField(null=True, blank=True)
    scraped_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)
    image_generated = models.BooleanField(default=False)
    instagram_posted = models.BooleanField(default=False)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.title
