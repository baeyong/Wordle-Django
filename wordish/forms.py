from django import forms

class targetForm(forms.Form):
    target_text = forms.CharField(label="New Target", max_length=5)

class guessForm(forms.Form):
    guess_text  = forms.CharField(label="Guess Word", max_length=5)






