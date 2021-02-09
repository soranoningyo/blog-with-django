from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,UserUpdaterForm,ProfileUpdaterForm


def register(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get("username")
      messages.success(request,f"{username} account is created successfully")
      login(request,user)
      return redirect("profile")
  else:
    form = RegistrationForm()
  return render(request,"auth_system/registration.html",{"form":form})

@login_required
def profile(request):
  if request.method == "POST":
    uu_form = UserUpdaterForm(request.POST,instance=request.user)
    pu_form = ProfileUpdaterForm(request.POST,request.FILES,instance=request.user.profile)
    if uu_form.is_valid() and pu_form.is_valid():
      uu_form.save()
      pu_form.save()
      messages.success(request,"an account is updated successfully")
      return redirect("profile")
  else:
    uu_form = UserUpdaterForm(instance=request.user)
    pu_form = ProfileUpdaterForm(instance=request.user.profile)
  context = {
    "uu_form":uu_form,
    "pu_form":pu_form
  }
  return render(request,"auth_system/profile.html",context=context)