from django import forms
from .models import Chat, UserProfile,Community

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'age', 'speak_lang', 'it_lang']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'age': forms.NumberInput(attrs={'min': 0}),
            'speak_lang': forms.Select(),
            'it_lang': forms.Select(),
        }
        labels = {
            'bio': '自己紹介',
            'age': '年齢',
            'speak_lang': '話す言語',
            'it_lang': 'プログラミング言語'
        }

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']
