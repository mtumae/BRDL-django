from django import forms
from .models import Post, SopaForm, OlengaiForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']



class SopaCourtForm(forms.ModelForm):
    class Meta:
        model = SopaForm
        fields = "__all__"

class OlengaiThForm(forms.ModelForm):
    class Meta:
        model = OlengaiForm
        fields = "__all__"