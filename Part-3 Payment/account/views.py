from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseBadRequest

from .tokens import account_activation_token
from .forms import RegistrationForm, UserEditForm, PwdResetConfirmForm
from .models import UserBase
from orders.views import user_orders


@login_required
def dashboard(request):
    orders = user_orders(request)
    print('account.views.dashboard')
    print(orders)
    return render(request,
                  'account/user/dashboard.html',
                  {'section': 'profile', 'orders': orders})


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'account/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')


def account_register(request):

    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            # setup emaill
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')

    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')


# @user_passes_test(lambda u: not u.is_authenticated, login_url='account:dashboard')
# def account_password_reset_confirm(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = UserBase.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, UserBase.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         if request.method == 'POST':
#             form = PwdResetConfirmForm(request.POST)
#             if form.is_valid():
#                 new_password = form.cleaned_data['new_password1']
#                 user.set_password(new_password)
#                 user.is_active = True  # Activate the user after password reset
#                 user.save()
#                 return redirect('account:password_reset_complete')
#         else:
#             form = PwdResetConfirmForm()

#         return render(request, 'account/user/password_reset_confirm.html', {'form': form})
#     else:
#         return HttpResponseBadRequest('Invalid reset link')
