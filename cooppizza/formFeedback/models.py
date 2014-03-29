from django import forms
import datetime

# Create your models here.

class FeedbackForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)


    def clean_observacoes(self):
        message = self.cleaned_data['observacoes']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message


"""class FeedbackForm(forms.Form):
	assunto = forms.CharField(max_length=100)
	dataDoFeedback =  forms.DateTimeField(initial=datetime.date.today)
	tipoDePedido = forms.CharField(max_length=100, required=False)
	formaDePedido = forms.CharField(max_length=100, required=False)
	precoPedido = forms.DecimalField(max_digits=7 , decimal_places=2, required=False)
	observacoes = forms.CharField(widget=forms.Textarea, required=False)
	nota = forms.DecimalField(max_digits=1)"""