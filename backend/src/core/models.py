from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100)
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


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_date = models.DateField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment


class Like(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
