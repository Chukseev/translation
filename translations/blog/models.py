from django.db import models


class BlogEntry(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'blog entries'

    def __str__(self):
        return self.name


class BlogImage(models.Model):
    blog_entry = models.ForeignKey(BlogEntry, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')
    description_for_image = models.CharField(max_length=100)

    def __str__(self):
        return f"Image for {self.blog_entry.name}"