from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Human
from django.contrib import messages
from .forms import HumanRegisterForm, HumanEditForm


# Create your views here.
def say_hello(request):
    return HttpResponse('hello user..')


def user_login(request):
    all_humans = Human.objects.all()
    return render(request, 'login.html', context={'all': all_humans})


def user_detail(request, human_id):
    h = Human.objects.get(id=human_id)
    return render(request, 'detail.html', context={'human': h})


def user_delete(request, human_id):
    Human.objects.get(id=human_id).delete()
    messages.success(request, 'user deleted successfully', extra_tags='success')
    return redirect('logins')


def user_register(request):
    if request.method == 'POST':
        form = HumanRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Human.objects.create(name=cd['name'], family=cd['family'], age=cd['age'], address=cd['address'],
                                 register_date=cd['register_date'])
            messages.success(request, 'user created successfully', extra_tags='success')
            return redirect('logins')
    else:
        form = HumanRegisterForm()
        return render(request, 'register.html', context={'form': form})


def user_edit(request, human_id):
    h = Human.objects.get(id=human_id)
    if request.method == 'POST':
        form = HumanEditForm(request.POST,instance=h)
        if form.is_valid():
            form.save()
            messages.success(request, 'user updated successfully', extra_tags='success')
            return redirect('details',human_id)
    else:
        form = HumanEditForm(instance=h)
        return render(request, 'edit.html', context={'form': form})
