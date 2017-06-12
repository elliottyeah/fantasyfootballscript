from django import forms

class SelecterForm(forms.Form):

        position = forms.ChoiceField(label='Pos', choices=[("Forward","Forward"),("Midfielder","Midfielder"),("Defender","Defender"),
            ("Goalkeeper","Goalkeeper")],
            widget = forms.Select(attrs={'class':"selectpicker show-tick form-control",'single title':"Position"}))

        cash = forms.ChoiceField(label='Cash',choices=[(x/10.0, x/10.0) for x in xrange(140, 40,-1)],
            widget = forms.Select(attrs={'class':"selectpicker show-tick form-control",'single title':"Budget"}))


class ContactForm(forms.Form):

    contact_name = forms.CharField(required=True,
        widget = forms.TextInput(attrs={'class':"form-control",'placeholder':'Name'}))
    contact_email = forms.EmailField(required=True,
        widget = forms.TextInput(attrs={'class':"form-control",'placeholder':'Email'}))
    content = forms.CharField(required=True,
                    widget = forms.Textarea(attrs={'class':"form-control",'rows':"3",'placeholder':'Message'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name:"
        self.fields['contact_email'].label = "Email:"
        self.fields['content'].label ="Message?"



