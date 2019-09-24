from django import forms
from tinymce import TinyMCE
from .models import Post, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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

    class Meta:
        model = Profile
        fields = (
            'bio',
            'location',
            'birth_date',
            'profile_picture'
        )


class UserForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.h(attrs={"name": "username",
    #                                                         "id": "username",
    #                                                         "placeholder": "username",
    #                                                         "class": "form-control",
    #                                                         "row": 1
    #                                                         }), label='Username')

    # email = forms.CharField(attrs={"name": "email",
    #                                "id": "email",
    #                                "placeholder": "email",
    #                                "class": "form-control",
    #                                }, label='Email')

    # first_name = forms.CharField(attrs={"name": "first_name",
    #                                     "id": "first_name",
    #                                     "placeholder": "first name",
    #                                     "class": "form-control",
    #                                     }, label='First Name')

    # last_name = forms.CharField(widget=Input(attrs={"name": "last_name",
    #                                                 "id": "last_name",
    #                                                       "placeholder": "last name",
    #                                                       "class": "form-control",
    #                                                 }), label='Last name')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )
