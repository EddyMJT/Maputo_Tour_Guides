from django import forms
from . models import Topic, Entry


class TopicForm(forms.ModelForm):

    class Meta:

        model = Topic
        fields = ['title', 'image']


class EntryForm(forms.ModelForm):

    class Meta:

        model = Entry
        fields = ['title', 'text', 'image']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'col': 80, 'style': 'width: 1357px; height: 400px;'})}