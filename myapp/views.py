from django.shortcuts import render,get_object_or_404
from .models import Measurement
from .forms import MeasurementForm
# Create your views here.


def index(request):
    obj = get_object_or_404(Measurement,id=1)
    if request.method == 'POST':
        form = MeasurementForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.destination = form.cleaned_data.get('destination')
            instance.location = 'Dehli'
            instance.distance = 70.1
            instance.save() 
    context = {'obj':obj,'form':MeasurementForm()}
    return render(request,"index.html",context)