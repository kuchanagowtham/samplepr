from django.shortcuts import render
from app.forms import MyregistrationForm
from app.models import Myregistration

def register(request):
	forms = MyregistrationForm()
	return render(request, 'home.html',{'forms': forms})

def savedata(request):
    forms = MyregistrationForm()  # Move this line outside the if statement

    if request.method == "POST":
        forms = MyregistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            forms = MyregistrationForm()  # Reset the form after saving
            return render(request, 'home.html', {'forms': forms})
    return render(request, 'home.html', {'forms': forms})


