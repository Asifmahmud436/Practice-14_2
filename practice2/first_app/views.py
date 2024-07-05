from django.shortcuts import render
from first_app.forms import Practice_2_form

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Practice_2_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Practice_2_form()
    return render(request,'home.html',{'form': form})
