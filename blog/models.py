from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    #header_image = models.ImageField(null=True, blank=True, upload_to='post_pic')
    content = RichTextField(blank=True, null=True)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


        # img = Image.open(self.header_image.path)
        #
        # if img.height > 1200 or img.width > 1200:
        #
        #     output_size = (1200, 1200)
        #     img.thumbnail(output_size)
        #     img.save(self.header_image.path)
        #
        # elif img.height < 1200 or img.width < 1200:
        #     output_size = (1200, 1200)
        #     img.thumbnail(output_size)
        #     img.save(self.header_image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



