from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = "Ngoc Dai"

    args = {'myName':name, 'numbers':numbers}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()

        agrs = {'form':form}
        return render(request, 'accounts/reg_form.html', agrs)