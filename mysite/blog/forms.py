from django import forms
from blog.models import Posting
from blog.models import User



class NewPost(forms.ModelForm):
    class Meta:
        model = Posting
        fields = '__all__'

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
