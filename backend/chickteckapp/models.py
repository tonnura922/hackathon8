from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Chat(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.sender} to {self.receiver}: {self.message[:20]}'


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