import os

import pandas as pd

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from .forms import Persona

def index(request):
    return render(request, "index.html")

def personas(request):
    personas = pd.read_csv("data/500_Person_Gender_Height_Weight_Index.csv")
    context = {
        "personas": personas,
        "estadisticas":{
            "Peso medio": personas["Peso"].mean,
            "Peso maximo": personas["Peso"].max,
            "Peso minimio": personas["Peso"].min,
            "Altura media": personas["Altura"].mean,
            "Peso maxima": personas["Altura"].max,
            "Peso minima": personas["Altura"].min
        }

    }
    return render(request, "persona_lista.html", context)

def nueva_persona(request):
    if request.method == 'POST':
        form = Persona(request.POST)
        if form.is_valid():
            df = pd.DataFrame(form.cleaned_data, index=[0])
            output_path = "data/500_Person_Gender_Height_Weight_Index.csv"
            df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)
            return HttpResponseRedirect("personas")
    else:
        form = Persona()
    return render(request, "nueva_persona.html", {"form":form})