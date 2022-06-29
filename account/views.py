from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from account.forms import AccountForm, AccountUpdateForm
from account.models import Account
from account.forms import RegisterForm, AccountAuthenticationForm


@login_required
def home(request):
    context = {}
    user = request.user
    sidebar = Account.objects.filter(id=user.id)
    context['sidebar'] = sidebar
    return render(request, 'home.html', context)


@login_required
def update_account(request, pk):
    context = {}
    user = request.user
    sidebar = Account.objects.filter(id=user.id)
    context['sidebar'] = sidebar

    if not user.is_authenticated:
        return redirect('account:signin')

    account_info = get_object_or_404(Account, pk=pk)

    if str(account_info.email) != str(user):
        return HttpResponse('Sorry, it is not your account.')

    if request.POST:
        form = AccountForm(request.POST or None, request.FILES or None, instance=account_info)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['message'] = 'Updated Successfully!'
            account_info = obj
            return redirect('account:home_page')

    form = AccountForm(
        initial={
            'email': account_info.email,
            'f_name': account_info.f_name,
            'l_name': account_info.l_name,
            'user_name': account_info.user_name,
            'image': account_info.image,
            'age': account_info.age,
            'date_birthday': account_info.date_birthday,
            'phone_number': account_info.phone_number
        }
    )
    account = Account.objects.filter(id=user.id)
    context['account'] = account
    context['form'] = form
    return render(request, 'personal_info.html', context)



def registration_view(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('account:home_page')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'sign_up.html', context)


def authentication(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('account:home_page')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('account:home_page')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'sign_in.html', context)


def signout_view(request):
    logout(request)
    return redirect('account:signin')
