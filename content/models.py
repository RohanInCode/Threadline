from django.db import models
from django.utils import timezone


class Category(models.Model):
    name        = models.CharField(max_length=100)
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def to_dict(self):
        """Return a plain dict matching the mock_data shape used in templates."""
        return {
            'id':          self.pk,
            'name':        self.name,
            'slug':        self.slug,
            'description': self.description,
        }


class Article(models.Model):
    STATUS_CHOICES = [
        ('draft',     'Draft'),
        ('published', 'Published'),
    ]

    title      = models.CharField(max_length=300)
    slug       = models.SlugField(unique=True, max_length=300)
    excerpt    = models.TextField(blank=True)
    content    = models.TextField(blank=True)
    image      = models.URLField(max_length=500, blank=True)
    author     = models.CharField(max_length=150, blank=True)
    category   = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
        to_field='slug',
    )
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    featured   = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def to_dict(self):
        """Return a plain dict matching the mock_data shape used in templates."""
        return {
            'id':         self.pk,
            'title':      self.title,
            'slug':       self.slug,
            'excerpt':    self.excerpt,
            'content':    self.content,
            'image':      self.image,
            'author':     self.author,
            'category':   self.category.slug if self.category else '',
            'status':     self.status,
            'featured':   self.featured,
            'created_at': self.created_at.strftime('%B {day}, %Y').format(day=self.created_at.day) if self.created_at else '',
        }
