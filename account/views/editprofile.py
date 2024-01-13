from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.forms import EditProfileForm

@login_required(login_url='/')
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('editprofile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'account/editprofile.jinja', context={
        'form':form,
    })