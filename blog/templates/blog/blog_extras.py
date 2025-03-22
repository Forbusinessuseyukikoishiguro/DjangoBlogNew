# blog/templatetags/blog_extras.py
from django import template
import re

register = template.Library()

@register.filter
def youtube_id(url):
    """YouTubeのURLからビデオIDを抽出する"""
    youtube_regex = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
    match = re.search(youtube_regex, url)
    if match:
        return match.group(1)
    return ''