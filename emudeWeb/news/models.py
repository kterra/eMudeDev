from django.db import models
from django_markdown.models import MarkdownField
from django.template.defaultfilters import slugify


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 200)
    subtitle = models.CharField(max_length = 400, blank = True)

    #Let's test with a text. TODO: change to user model
    author = models.CharField(max_length = 100)
    body = MarkdownField()

    publication_date = models.DateTimeField(auto_now_add = True)
    last_modified_date = models.DateTimeField(auto_now_add = True)

    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
