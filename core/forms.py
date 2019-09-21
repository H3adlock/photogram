from django import forms
from tinymce import TinyMCE
from .models import Post, Comment, Profile


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget(
        attrs={'required': False, 'col': 30, 'rows': 10}))

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"name": "usercomment",
                                                           "id": "usercomment",
                                                           "placeholder": "Add a public comment",
                                                           "class": "form-control",
                                                           "rows": 1}), label='')

    class Meta:
        model = Comment
        fields = ('content',)


class ProfileForm(forms.ModelForm):
    # bio = CharField(label='New label')

    class Meta:
        model = Profile
        fields = '__all__'
