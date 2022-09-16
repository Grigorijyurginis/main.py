from django.shortcuts import render
from .models import Forms
from .forms import FormsForm

def form(request):
    a = Forms.objects.all()
    return render(request, 'form/form.html', {'a': a})
def index(request):
    return render(request, 'main/index.html')

def create (request):
    error = ''
    if request.method == 'POST':
        c = FormsForm(request.POST)
        if c.is_valid():
            c.save()
        else:
            error = 'Форма заполнена неверно'
    a = FormsForm()
    b = {
        'a': a,
        'error': error
    }
    return render(request, 'form/create.html', b)