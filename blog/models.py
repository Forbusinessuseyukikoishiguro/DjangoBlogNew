from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 音声ファイルとYouTube動画用のフィールドを追加
    audio_file = models.FileField(upload_to='audio/', null=True, blank=True)
    youtube_url = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})