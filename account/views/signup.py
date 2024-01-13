from django.shortcuts import render, redirect
from account.forms import SignupForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('index')
    else:
        form = SignupForm()

    return render(request, 'account/signup.jinja', context={
        'form':form,
    })