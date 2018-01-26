from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create a custom manager for the Post models
# to retrieve all posts that have been published
class PublishedManager(models.Manager):
    # get_queryset returns the queryset to be executed
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    # Create the constants for status. We used tuple because these
    # are immutable properties
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User,
        related_name='blog_posts',
        on_delete=models.PROTECT
        )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
        )

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Custom manager for published posts

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[
            self.publish.year,
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug
        ])
