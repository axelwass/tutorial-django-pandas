from django import forms

class Persona(forms.Form):
    genero = forms.ChoiceField(choices=[("Hombre", "Hombre"), ("Mujer","Mujer")])
    altura = forms.IntegerField(help_text="En centimetros", min_value=1)
    peso = forms.IntegerField(help_text="En gramos", min_value=1)
    indice = forms.ChoiceField(choices=[("0",0), ("1",1),("2",2), ("3",3), ("4",4), ("5",5)])