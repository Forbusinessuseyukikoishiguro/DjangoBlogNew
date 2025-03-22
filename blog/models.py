from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse  # この行を追加
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    audio_file = models.FileField(upload_to='audio/', blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    # この方法を追加
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']