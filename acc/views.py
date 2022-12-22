from django.shortcuts import render, redirect
from acc.forms import UserForm
from django.contrib.auth import authenticate, login

def signup(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      raw_password = form.cleaned_data.get('password1')
      #form.cleaned_data.get('is_superuser')
      user = authenticate(username=username, first_name=first_name, last_name=last_name, password=raw_password)
      login(request, user)
      return redirect('/')
  else:
    form = UserForm()
  return render(request, 'acc/signup.html', {'form':form})