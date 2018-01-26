from django import forms


class EmailPostForm(forms.Form):
    # name = forms.CharField(max_length=25, label='Name')
    name = forms.CharField(
        max_length=25,
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
        )
    email = forms.EmailField(
        label='From',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'To:Email'})
        )
    to = forms.EmailField(
        label='To',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'From: Email'})
        )
    comments = forms.CharField(
        required=False,
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
        )
