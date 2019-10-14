from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class NameForm(forms.Form):
    calculation_string = forms.CharField(label='calculation_string', max_length=100)

def index(request):
    result = 0
    if request.method == 'POST':
        print(request.POST)
        result = eval(str(request.POST["calculation_string"]))
        print(result, eval(request.POST["calculation_string"]),(request.POST["calculation_string"]))
        
    form = NameForm()

    return render(request, 'index.html', {'form': form, 'result': result})
