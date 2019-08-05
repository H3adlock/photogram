from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    # slug = models.SlugField(
    #     default='',
    #     editable=False,
    #     max_length=settings.BLOG_TITLE_MAX_LENGTH,
    # )

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('article-pk-slug-detail', kwargs=kwargs)

    # def save(self, *args, **kwargs):
    #     value = self.title
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)
