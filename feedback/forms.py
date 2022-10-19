from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Почта', required=True, widget=forms.TextInput(attrs={'class': 'form-label'}))
    name = forms.CharField(label='Имя', max_length=30, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-label'}))
    message = forms.CharField(label='Сообщение', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-label', 'style': 'padding-bottom:100px;'}))
