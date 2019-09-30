from django import forms
from tinymce import TinyMCE
from .models import Post, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.safestring import mark_safe


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        html = Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))


class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/customclearablefileinput.html'


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


class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.label != "Profile picture":
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = (
            'bio',
            'location',
            'birth_date',
            'profile_picture'
        )
        widgets = {
            'birth_date': DateInput(),
        }


class UserForm(forms.ModelForm):
    # last_name = forms.CharField(widget=Input(attrs={"name": "last_name",
    #                                                 "id": "last_name",
    #                                                       "placeholder": "last name",
    #                                                       "class": "form-control",
    #                                                 }), label='Last name')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )
