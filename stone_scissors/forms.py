from django import forms


class ChoiceForm(forms.Form):
    CHOICES = [
        ('Камень', 'Камень'),
        ('Ножницы', 'Ножницы'),
        ('Бумага', 'Бумага'),
    ]
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
