from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    SPEAK_LANG = (
        ('japanese', 'Japanese'),
        ('english', 'English'),
        ('chinese', 'Chinese'),
    )
    speak_lang = models.CharField(null=True, max_length=50, choices=SPEAK_LANG)

    IT_LANG = (
        ('python', 'Python'),
        ('c', 'C'),
        ('c++', 'C++'),
        ('c#', 'C#'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
    )
    it_lang = models.CharField(null=True, max_length=50, choices=IT_LANG)
